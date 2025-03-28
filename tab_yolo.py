from datetime import datetime
from email.message import EmailMessage
import os, base64, shutil, time, cv2, smtplib
import dash_bootstrap_components as dbc
from dash import dcc, html, callback_context, Output, Input, State, dash_table, no_update

class YoloModel:
    """
    Diese Klasse verwaltet die YOLO-Modelle und den Datensatz-Erstellungsprozess in der Dash-Anwendung.

    Funktionen:
    - Listet alle verfügbaren YOLO-Modelle auf und ermöglicht das Hochladen neuer Modelle.
    - Überwacht die Verbindungsstatus von Kamera und Roboter.
    - Generiert Bilddatensätze mit dem Quanser-Roboter (Makro- und Mikroaufnahmen).
    - Bietet die Möglichkeit, Datensätze als ZIP herunterzuladen oder per E-Mail zu versenden.
    """
    def __init__(self, app, qarm, camera):
        """
        Initialisiert die Klasse für die YOLO-Modellverwaltung.

        Args:
            app (Dash): Die Dash-App-Instanz.
            qarm (QArmControl): Instanz des Roboter-Controllers.
            camera (Camera): Instanz der Kamera-Klasse für Bilderfassung.
        """
        self.app = app
        self.yolo_model_dir = "YOLO_Modelle"
        self.qarm = qarm
        self.camera = camera
        self.current_yolo_model = ""
        self.layout = self.render_layout()
        self.callbacks()

    def render_layout(self):
        """
        Erstellt das Layout für die YOLO-Model-Verwaltung und Datensatzgenerierung.

        Enthält:
        - Eine Liste verfügbarer YOLO-Modelle und eine Upload-Funktion.
        - Buttons für die Bilddatensatzerstellung mit Makro- und Mikroaufnahmen.
        - Fortschrittsanzeigen für die Fotoaufnahme.
        - Die Möglichkeit, ZIP-Dateien herunterzuladen oder per E-Mail zu versenden.

        Returns:
            dbc.Container: Das vollständige Layout für diesen Tab.
        """
        return dbc.Container([
            # ----------------------------------------
            # Überschrift und Modellverwaltung
            # ----------------------------------------
            html.H4("YOLO Modell Verwaltung und Training", className="mt-3"),
            html.Hr(),

            # ----------------------------------------
            # Row 1: Links--> YOLO-Modell-Liste + Upload || Rechts--> Verbindungsstatus + Dropdown-Zip-Download
            # ----------------------------------------
            dbc.Row([
                # Links
                dbc.Col([
                    html.H5("Verfügbare YOLO Modelle:"),
                    dcc.Interval(id="yolo-model-list-interval", interval=2000, n_intervals=0),
                    # Modell-Liste
                    html.Div(id="yolo-model-list"),
                    # Upload-Button
                    dcc.Upload(
                        id="upload-yolo-model",
                        children=html.Div(["Modell hochladen"]),
                        style={
                            "width": "100%", "height": "50px", "lineHeight": "40px",
                            "borderWidth": "1px", "borderStyle": "dashed",
                            "borderRadius": "10px", "textAlign": "center", "margin": "10px"
                        },
                        multiple=False
                    ),
                    # Ladebalken solange hochgeladen wird
                    dcc.Loading(
                    id="loading-upload-status",
                    type="default",
                    children= html.Div(id="upload-status", style={"textAlign": "center", "marginTop": "25px"})
                    )
                ], width=6),
                # Rechts
                dbc.Col([
                    # Verbindungsstatus
                    html.H5(["Übersicht: ",
                            html.Span("Verbindungsstatus", id="connection-status-text", style={"color": "gray"})], style={"marginBottom": "5px"}),
                    html.Div(id="yolo-connection-status"),
                    dbc.Row([
                        dbc.Col([
                            # Dropdown-Zips
                            dcc.Dropdown(
                                id="dropdown-download-zips",
                                options=[
                                    {"label": f, "value": os.path.join("New_zips", f)}
                                    for f in os.listdir("New_zips")
                                    if os.path.isfile(os.path.join("New_zips", f))
                                ],
                                placeholder="Wähle eine ZIP-Datei",
                                style={"color": "black"}
                            )
                        ], width=9),
                        # Button zum herunterladen
                        dbc.Col([
                            dbc.Button("Herunterladen", id="btn-download-zip", color="success", style={"width": "100%", "textAlign": "center", "whiteSpace": "nowrap"})
                        ], width=3)
                    ], className="mb-2"),
                    dcc.Download(id="download-zip-file"),
                ], width=6)
            ], className="mb-4"),

            html.Hr(),

            # ----------------------------------------
            # Row 2: Datensatz generieren für YOLO-Training
            # ----------------------------------------
            html.H4("Datensatzgenerierung für YOLOv11-Modelltraining"),
            html.P("Dieser Bereich führt Schritt für Schritt durch die Erstellung eines individuellen Trainingsdatensatzes "
                "für das YOLOv11-Modell. Es ist empfehlenswert, die RGB-Live-Übertragung (aus dem Tab 'Live-Feed') in einem separaten Fenster zu öffnen. "
                "Dadurch lässt sich unmittelbar nachvollziehen, welche Aufnahmen der Roboter erstellt und wie der Datensatz "
                "später aussieht. Dieses Vorgehen ist besonders vorteilhaft, wenn das YOLO-Modell später in Verbindung mit dem "
                "Roboter verwendet wird, da die Bilder aus der exakten Roboterperspektive aufgenommen werden und somit optimale Ergebnisse liefern."),
            # Button Datensatz generieren --> erst freischalten wenn alle Geräte verbunden
            dbc.Row([
                dbc.Col([
                    dbc.Button("Datensatz generieren", id="btn-generate-dataset", color="primary", style={"width": "100%"})
                ], width={"size": 6, "offset": 3})
            ], className="mb-3"),
            html.Div(id="dataset-status", className="mb-3"),
            html.Hr(),

            # Hier wird der restliche Inhalt zunächst versteckt:
            html.Div(
                id="hidden-content",
                children=[
                    html.Hr(),

                    # ========== Abschnitt: Makroaufnahmen ==========
                    html.P("Schritt 1: Makroaufnahmen erstellen"),
                    html.P("Der Roboter befindet sich nun in der Makroposition, um eine Übersicht des Arbeitsbereichs aufzunehmen. "
                        "Bitte geben Sie an, wie viele Makroaufnahmen erstellt werden sollen:"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Input(id="input-macro-count", type="number", min=1,
                                    placeholder="Anzahl der Makroaufnahmen", value=None, className="mb-2")
                        ], width=9),
                        dbc.Col([
                            dbc.Progress(id="macro-progress", value=0, max=1, striped=True, animated=True, style={"height": "40px"})
                        ], width=3)
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Makroaufnahme erstellen", id="btn-capture-macro", color="primary", style={"width": "100%"})
                        ], width={"size": 6, "offset": 3})
                    ], className="mb-3"),
                    html.Div(id="macro-status", className="mb-3"),
                    html.Hr(),

                    # ========== Abschnitt: Mikroaufnahmen ==========
                    html.P("Schritt 2: Mikroaufnahmen erstellen:"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Mikroposition anfahren", id="btn-move-to-micro", color="primary", style={"width": "100%"})
                        ], width={"size": 6, "offset": 3})
                    ], className="mb-3"),
                    html.P("Der Roboter bewegt sich nun nah über der Arbeitsfläche - dies ist beabsichtigt und ungefährlich. "
                        "Bitte geben Sie an, wie viele Mikroaufnahmen erstellt werden sollen:"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Input(id="input-micro-count", type="number", min=1,
                                    placeholder="Anzahl der Mikroaufnahmen", value=None, className="mb-2")
                        ], width=9),
                        dbc.Col([
                            dbc.Progress(id="micro-progress", value=0, max=1, striped=True, animated=True, style={"height": "40px"})
                        ], width=3)
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Mikroaufnahme erstellen", id="btn-capture-micro", color="primary", style={"width": "100%"})
                        ], width={"size": 6, "offset": 3})
                    ], className="mb-3"),
                    html.Div(id="micro-status", className="mb-3"),
                    html.Hr(),

                    # ========== Abschluss: Roboter in Home-Position fahren und Daten erhalten ==========
                    html.H5("Schritt 3: Abschluss und Datensatzexport"),
                    html.P("Optional kann der erstellte Datensatz zusätzlich per E-Mail empfangen werden. Geben Sie hierfür Ihre "
                        "E-Mail-Adresse im folgenden Feld ein (z. B. my.mail@gmail.com):",
                        style={"textAlign": "center", "fontWeight": "bold"}
                    ),
                    dbc.Row([
                        dbc.Col([
                            dbc.Input(id="email-input", type="email", placeholder="E-Mail-Adresse eingeben", style={"width": "100%"})
                        ], width=6, className="offset-md-3")
                    ], className="mb-3"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Roboter zur Home-Position bewegen und Daten herunterladen", id="btn-home", color="primary", style={"width": "100%"})
                        ], width={"size": 6, "offset": 3})
                    ], className="mb-4"),
                    html.Div(id="home-status", className="mb-3"),
                    html.Hr(),

                    html.H5("Schritt 4: Datensatz annotieren und vorbereiten"),
                    html.P("Im nächsten Schritt muss der Datensatz annotiert und optional augmentiert werden, um "
                        "damit ein YOLOv11-Modell zu trainieren. Roboflow stellt hierfür eine hilfreiche Plattform "
                        "zur Verfügung:"),
                    html.A("Zur Roboflow-Plattform (extern öffnen)", href="https://roboflow.com", target="_blank"),
                    html.Hr(),

                    html.H5("Schritt 5: YOLOv11-Modelltraining auf Google Colab"),
                    html.P("Der annotierte Datensatz kann nun verwendet werden, um ein YOLOv11-Modell auf Google Colab zu trainieren. "
                        "Das folgende Colab-Notebook unterstützt diesen Vorgang optimal (GPU-Empfehlung: T4, ca. 4 Std./Tag):"),
                    html.A("YOLOv11-Training-Notebook auf Google Colab öffnen", href="https://colab.research.google.com/drive/1WRka45oVjYHb9bVyH7-4ziOp1pnaCRof?usp=sharing", target="_blank"),
                    html.Hr(),

                    html.H5("Schritt 6: Upload und Nutzung des trainierten YOLOv11-Modells"),
                    html.P("Nach Abschluss des Trainings steht das beste Modell ('best.pt') zum Upload im oberen Bereich zur Verfügung. "
                        "Nach erfolgreichem Upload kann das YOLO-Modell direkt in der Applikation ausgewählt und verwendet werden."),
                ],
                style={"display": "none"}  # Anfangs ausgeblendet
            ),
            dcc.Download(id="zip-download"),
        ], fluid=True)


    def callbacks(self):
        """
        Registriert alle Callbacks für die YOLO-Modellverwaltung und die Datensatzgenerierung.
        """

        # ------------------------------
        # Callback 1: Freischaltung des Datensatz-Generierungsbereichs
        @self.app.callback(
            Output("hidden-content", "style"),
            [Input("btn-generate-dataset", "n_clicks")],
            [State("btn-generate-dataset", "disabled")]
        )
        def show_hidden_content(n_clicks, disabled):
            if n_clicks and not disabled:
                # Leere Ordner "New_imgs/makro" und "New_imgs/mikro"
                for directory in ["New_imgs/makro", "New_imgs/mikro"]:
                    if os.path.exists(directory):
                        for fname in os.listdir(directory):
                            fpath = os.path.join(directory, fname)
                            if os.path.isfile(fpath) or os.path.islink(fpath):
                                os.unlink(fpath)
                            elif os.path.isdir(fpath):
                                shutil.rmtree(fpath)
                self.qarm.go_to((0.3, 0.001, 0.175)) # Fahre Roboter in Makroposition
                return {"display": "block"} # Sichtbar machen
            return {"display": "none"}

        # ------------------------------
        # Callback 2: Aktualisiere verfügbare YOLO-Modell-Liste (alle 2s)
        @self.app.callback(
            Output("yolo-model-list", "children"),
            [Input("yolo-model-list-interval", "n_intervals"),
             Input("yolo-dropdown", "value")]
        )
        def update_model_list(n_intervals, yolo_value):
            self.current_yolo_model = yolo_value
            try:
                files = os.listdir(self.yolo_model_dir)
                model_files = [f for f in files if f.endswith(".pt")] # nur .pt files anzeigen
                if model_files:
                    items = []
                    for f in model_files:
                        # aktuelles Modell in grüner Schrift
                        if f == self.current_yolo_model:
                            items.append(html.Li(html.Span(f, style={"color": "green"})))
                        else:
                            items.append(html.Li(f))
                    return html.Ul(items)
                else:
                    return "Keine Modelle gefunden."
            except Exception as e:
                return f"Fehler: {str(e)}"

        # ------------------------------
        # Callback 3: Upload von YOLO-Modellen
        @self.app.callback(
            Output("upload-status", "children"),
            Input("upload-yolo-model", "contents"),
            State("upload-yolo-model", "filename")
        )
        def upload_model(upload_contents, upload_filename):
            if upload_contents:
                if not upload_filename.lower().endswith(".pt"): # nur .pt erlauben
                    return "Fehler: Das YOLO-Model muss als .pt-Datei hochgeladen werden."
                content_type, content_string = upload_contents.split(',')
                decoded = base64.b64decode(content_string)
                filepath = os.path.join(self.yolo_model_dir, upload_filename)
                try:
                    with open(filepath, "wb") as f:
                        f.write(decoded)
                    return f"Modell {upload_filename} erfolgreich hochgeladen."
                except Exception as e:
                    return f"Fehler beim Speichern: {str(e)}"
            return ""

        # ------------------------------
        # Callback 4: Aktualisiere Verbindungsstatus (Kamera & Roboter)
        @self.app.callback(
            Output("yolo-connection-status", "children"),
            [Input("cam-icon", "className"),
             Input("robot-icon", "className")]
        )
        def update_connection_status(cam_status, robot_status):
            statuses = []
            if cam_status == "connected":
                statuses.append("Kamera verbunden.")
            else:
                statuses.append("Kamera nicht verbunden - Verbindung erforderlich.")
            if robot_status == "connected":
                statuses.append("Roboter verbunden.")
            else:
                statuses.append("Roboter nicht verbunden - Verbindung erforderlich.")
            return html.Ul([html.Li(s) for s in statuses])

        # ------------------------------
        # Callback 5: Download manuell Zip-Datei
        @self.app.callback(
            Output("download-zip-file", "data"),
            Input("btn-download-zip", "n_clicks"),
            State("dropdown-download-zips", "value"),
            prevent_initial_call=True
        )
        def download_zip_file(n_clicks, selected_file):
            if selected_file and os.path.exists(selected_file):
                return dcc.send_file(selected_file)
            return no_update

        # ------------------------------
        # Callback 6: Aktiviere den Button "Datensatz generieren", wenn Kam+Robo verbunden
        @self.app.callback(
            Output("btn-generate-dataset", "disabled"),
            [Input("cam-icon", "className"),
             Input("robot-icon", "className")]
        )
        def update_generate_button(cam_status, robot_status):
            if cam_status == "connected" and robot_status == "connected":
                return False
            return True

    # ------------------------------------------------------------------------------------
    # ----------------------- NACH Datensatz generieren Button ---------------------------
    # ------------------------------------------------------------------------------------

        # ------------------------------
        # Callback 7: Makro-Fotos + Fortschrittsbalken
        @self.app.callback(
            [Output("macro-status", "children"),
            Output("macro-progress", "value")],
            Input("btn-capture-macro", "n_clicks"),
            State("input-macro-count", "value")
        )
        def capture_macro(n_clicks, macro_total):
            # mindestens 1 Foto
            if macro_total is None or macro_total < 1:
                return "Bitte nehmen Sie mindestens 1 Foto auf.", no_update

            directory = os.path.join("New_imgs", "makro")
            current_value = len(os.listdir(directory))

            ctx = callback_context
            if not ctx.triggered:
                progress = current_value / macro_total if macro_total and macro_total > 0 else 0
                return "", progress
            
            # wenn max Anzahl erreicht, keine weitere Aufnahme
            if current_value >= macro_total:
                return f"Sie haben bereits {macro_total}/{macro_total} Fotos aufgenommen. Fahren Sie jetzt fort.", current_value

            # Foto aufnehmen
            if n_clicks:
                image, _ = self.camera.get_stream()
                if image is None:
                    return "Fehler beim Aufnehmen des Makrofotos.", current_value

                timestamp = int(time.time())
                filename = os.path.join("New_imgs", "makro", f"macro_{timestamp}.jpg")
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                cv2.imwrite(filename, image)

                current_value = len(os.listdir(directory))
                fraction = current_value / macro_total  # Anteil ProgessBar
                return f"Makrofoto aufgenommen: {filename} ({current_value}/{macro_total})", fraction

            return no_update, current_value / macro_total

        # ------------------------------
        # Callback 8: Mikroposition, Foto und Fortschrittsbalken
        @self.app.callback(
            [Output("micro-status", "children"),
            Output("micro-progress", "value")],
            [Input("btn-move-to-micro", "n_clicks"),
            Input("btn-capture-micro", "n_clicks")],
            State("input-micro-count", "value")
        )
        def micro_actions(n_move, n_capture, micro_total):
            directory = os.path.join("New_imgs", "mikro")
            current_value = len(os.listdir(directory))
            
            ctx = callback_context
            if not ctx.triggered:
                progress = current_value / micro_total if micro_total and micro_total > 0 else 0
                return "", progress

            triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            # Mikroposition anfahren
            if triggered_id == "btn-move-to-micro":
                micro_coord = (0.3, 0.001, 0.01) # getestet
                self.qarm.go_to(micro_coord)
                return "Roboter in Mikroposition gefahren.", current_value or 0

            # Fotos aufnehmen
            elif triggered_id == "btn-capture-micro":
                if micro_total is None or micro_total < 1:
                    return "Bitte nehmen Sie mindestens 1 Mikrofoto auf.", no_update
                
                if current_value >= micro_total:
                    return f"Sie haben bereits {micro_total}/{micro_total} Mikrofotos aufgenommen. Fahren Sie jetzt fort.", current_value
                
                image, _ = self.camera.get_stream()
                if image is None:
                    return "Fehler beim Aufnehmen des Mikrofotos.", current_value

                timestamp = int(time.time())
                filename = os.path.join("New_imgs", "mikro", f"micro_{timestamp}.jpg")
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                cv2.imwrite(filename, image)
                
                current_value = len(os.listdir(directory))
                progress = current_value / micro_total if micro_total and micro_total > 0 else 0
                return f"Mikrofoto aufgenommen: {filename} ({current_value}/{micro_total})", progress

            return "", current_value / micro_total if micro_total and micro_total > 0 else no_update

        # ------------------------------
        # Callback 9: Home-Position und Daten herunterladen + optional per Mail schicken
        @self.app.callback(
            [Output("home-status", "children"),
             Output("zip-download", "data")],
            [Input("btn-home", "n_clicks")],
            [State("email-input", "value")]
        )
        def home_and_download(n_clicks, recipient_email):
            if n_clicks:
                self.qarm.go_to("home")
                timestamp = datetime.now().strftime("%H-%M--%d-%m-%Y")
                zip_basename = os.path.join("New_zips", f"zip_{timestamp}")
                shutil.make_archive(zip_basename, 'zip', "New_imgs")
                zip_filepath = f"{zip_basename}.zip"
                
                download = dcc.send_file(zip_filepath) # download triggern

                # Falls eine E-Mail-Adresse eingegeben wurde, ZIP senden
                if recipient_email:
                    try:
                        send_zip_via_email(zip_filepath, recipient_email)
                        status = f"Roboter in Home-Position gefahren. ZIP-Datei '{zip_filepath}' erstellt und per E-Mail verschickt."
                    except Exception as e:
                        status = f"ZIP-Datei '{zip_filepath}' erstellt, aber E-Mail Versand schlug fehl: {str(e)}"
                else:
                    status = f"Roboter in Home-Position gefahren. ZIP-Datei '{zip_filepath}' wurde erstellt."
                return status, download
            return "", no_update

        def send_zip_via_email(zip_filepath, recipient_email):
            """
            Versendet eine ZIP-Datei als E-Mail-Anhang.

            Args:
                zip_filepath (str): Pfad zur ZIP-Datei, die gesendet werden soll.
                recipient_email (str): E-Mail-Adresse des Empfängers.

            Raises:
                Exception: Falls der E-Mail-Versand fehlschlägt.
            """
            msg = EmailMessage()
            msg["Subject"] = "Ihre gewünschte ZIP-Datei"
            msg["From"] = "quanserstrgsappmailservice@gmail.com"
            msg["To"] = recipient_email
            msg.set_content("Anbei erhalten Sie die ZIP-Datei.")

            # ZIP-Datei als Anhang hinzufügen
            with open(zip_filepath, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(zip_filepath)
            msg.add_attachment(file_data, maintype="application", subtype="zip", filename=file_name)

            # Sende E-Mail via SMTP
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login("quanserstrgsappmailservice@gmail.com", "gsbs podx xpgp tgyz")
                smtp.send_message(msg)

        