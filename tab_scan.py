import os, base64
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html, callback_context, Output, Input, State, dash_table, no_update
from scan_manager import ScanManager, create_birdseye_map

class Scan:
    """
    Diese Klasse verwaltet den "Scan"-Tab der Dash-Anwendung.

    Funktionen:
    - Führt einen Scan-Vorgang mit dem Quanser 4-DOF Roboter aus.
    - Zeigt eine Tabelle mit den erkannten Objekten und deren Positionen.
    - Stellt eine Vogelperspektiven-Karte der Objekte im Arbeitsbereich dar.
    - Zeigt die Scanaufnahmen des Roboters mit Boundary-Boxen und Labels.
    - Erlaubt Pick & Place-Aktionen zwischen Objekten oder zu bestimmten Koordinaten.
    """
    def __init__(self, app, qarm, camera, mysql_manager):
        """
        Initialisiert die Scan-Klasse.

        Args:
            :param app: Die Dash-App-Instanz.
            :param qarm: Instanz des QArmControl (Roboter).
            :param camera: Instanz der Camera-Klasse.
            :param mysql_manager: Instanz des MySQL-Managers.
        """
        self.app = app
        self.qarm = qarm
        self.camera = camera
        self.mysql_manager = mysql_manager
        self.layout = self.render_layout()
        self.register_callbacks()

    def render_layout(self):
        """
        Erstellt das Layout für den "Scan"-Tab.

        Enthält:
        - Verbindungsstatus und Scan-Button.
        - Tabelle mit Scan-Ergebnissen.
        - Vogelperspektiven-Karte zur Visualisierung der Objekte.
        - Scan-Bilder mit Boundary-Boxen und Labels.
        - Steuerung für Pick & Place-Aktionen.

        Returns:
            dbc.Container: Layout für den Scan-Tab.
        """
        return dbc.Container([        
            # -----------------------------------------
            # Row 1: Links--> Status-Text || Rechts--> SCAN-Button
            # -----------------------------------------
            dbc.Row([
                dbc.Col([
                    html.H4([
                        "Übersicht: ",
                        html.Span("Verbindungsstatus", id="connection-status-text", style={"color": "gray"})
                    ], style={"marginBottom": "5px"}),
                    html.Div(id="scan-status-text")
                ], width=6),
                dbc.Col([
                    dbc.Button("SCAN", id="btn-scan", color="success", disabled=True, style={"width": "150px", "height":"120px"}),
                    dcc.Loading(
                        id="loading-scan-status",
                        type="default",
                        children=[html.Div(id="scan-action-status")],
                        style={"marginTop": "50px"}
                    )
                ], width=6,  className="d-flex flex-column justify-content-center align-items-center", style={"paddingLeft": "30px"})
            ], className="mb-3"),

            # -----------------------------------------
            # Row 2: Container für die Scan-Ergebnisse (als DataTable)
            # -----------------------------------------
            dbc.Row([
                dbc.Col([
                    html.H4("Scan Ergebnisse:"),
                    html.Div(id="scan-results-container")
                ], width=12)
            ]),
            
            # -----------------------------------------
            # Row 3: Links--> Birdseye Map || Rechts--> Scan-Bilder
            # -----------------------------------------
            dbc.Row([
                dbc.Col([
                    html.H4("Vogelperspektive der Objekte:", className="text-center"),
                    dcc.Graph(id="birdseye-map", style={"width": "80%", "height": "auto"},
                              config={"responsive": True}  # Erlaubt Plotly, das Diagramm an die verfügbare Breite anzupassen
                        )
                ], width=6, className="d-flex flex-column justify-content-center align-items-center"),
                dbc.Col([
                    html.H4("Scan-Bilder", className="text-center"),
                    html.Div(id="scan-images-container"),
                    dbc.Button("Bilder aktualisieren", id="refresh-scan-images", color="secondary", size="lg", style={"marginTop": "10px"})
                ], width=6, className="d-flex flex-column justify-content-center align-items-center")
            ]),
            html.Hr(),
            # kleine Textausgabe für Status bei Pick&Place
            dbc.Col([
                html.Div(id="placement-status", style={"marginTop": "10px"})
            ]),

            # -----------------------------------------
            # Row 4: Pick & Place Funktionen
            # -----------------------------------------
            dbc.Row([
                dbc.Col([
                    html.Div(id="pick-place-controls", children=[
                        dbc.Row([
                            dbc.Col([
                                html.H5("Platziere Objekt A zu Objekt B:"),
                                dbc.Row([
                                    dbc.Col([
                                        dcc.Dropdown(id="placement-dropdown-1", options=[], placeholder="Objekt A auswählen", style={"color": "black"})
                                    ], width=6),
                                    dbc.Col([
                                        dcc.Dropdown(id="placement-dropdown-2", options=[], placeholder="Objekt B auswählen", style={"color": "black"})
                                    ], width=6)
                                ], className="mb-2"),
                                dbc.Button("Ausführen", id="btn-place-objects-compare", color="primary")
                            ], width=12)
                        ]),
                        dbc.Row([
                            dbc.Col([
                                html.H5("Platziere Objekt A zu bestimmten Koordinaten:"),
                                dbc.Row([
                                    dbc.Col([
                                        dcc.Dropdown(id="placement-dropdown-single", options=[], placeholder="Objekt A auswählen", style={"color": "black"})
                                    ], width=6),
                                    dbc.Col([
                                        dbc.Input(id="placement-x", type="number", placeholder="X", min=-0.75, max=0.75, step=0.001)
                                    ], width=3),
                                    dbc.Col([
                                        dbc.Input(id="placement-y", type="number", placeholder="Y", min=-0.75, max=0.75, step=0.001)
                                    ], width=3)
                                ], className="mb-2"),
                                dbc.Button("Ausführen", id="btn-place-object-coord", color="primary")
                            ], width=12)
                        ])
                    ], style={"display": "block", "marginTop": "20px"})
                ])
            ]),

        ], fluid=True)
    
    def register_callbacks(self):
        """Registriert alle Callbacks für den Scan-Tab."""

        # --------------------------------- Statusanzeigen -----------------------------------
        # CALLBACK 1: Aktivierung des Scan-Buttons basierend auf den Systemverbindungen
        @self.app.callback(
            Output("btn-scan", "disabled"),
            [Input("robot-icon", "className"),
             Input("cam-icon", "className"),
             Input("db-icon", "className"),
             Input("yolo-dropdown", "value")]
        )
        def update_scan_button(robot_status, cam_status, db_status, yolo_value):
            if robot_status == "connected" and cam_status == "connected" and db_status == "connected" and yolo_value:
                return False
            return True
        

        # CALLBACK 2: Aktualisierung der Statusanzeige
        @self.app.callback(
            Output("scan-status-text", "children"),
            [Input("robot-icon", "className"),
             Input("cam-icon", "className"),
             Input("db-icon", "className"),
             Input("yolo-dropdown", "value")]
        )
        def update_scan_status_text(robot_status, cam_status, db_status, yolo_value):
            statuses = []
            if robot_status == "connected":
                statuses.append("Roboter verbunden.")
            else:
                statuses.append("Der Roboter ist nicht verbunden - dieser wird für den Scan Vorgang benötigt. Bitte stellen Sie eine Verbindung her.")
            
            if cam_status == "connected":
                statuses.append("Kamera verbunden.")
            else:
                statuses.append("Die Kamera ist nicht verbunden - diese wird für den Scan Vorgang benötigt. Bitte stellen Sie eine Verbindung her.")
            
            if db_status == "connected":
                statuses.append("SQL-Server verbunden.")
            else:
                statuses.append("Der SQL-Server ist nicht verbunden - dieser wird für den Scan Vorgang benötigt. Bitte stellen Sie eine Verbindung her.")
            
            if yolo_value:
                statuses.append(f"Aktuell genutztes Modell: {yolo_value}")
            else:
                statuses.append("Kein YOLO Modell ausgewählt.")
            
            # Erzeuge eine ungeordnete Liste (UL) mit den Statusmeldungen als Listenelemente (LI)
            return html.Ul([html.Li(item) for item in statuses])
        
        # CALLBACK 3: Einfärben von "Verbindungsstatus"
        @self.app.callback(
            Output("connection-status-text", "style"),
            [Input("db-icon", "className"),
            Input("cam-icon", "className"),
            Input("robot-icon", "className")]
        )
        def update_connection_status_color(db_status, cam_status, robot_status):
            statuses = [db_status, cam_status, robot_status]
            connected_count = statuses.count("connected")
            if connected_count == 3:
                return {"color": "green"}
            elif connected_count == 0:
                return {"color": "red"}
            else:
                return {"color": "yellow"}
        

        # --------------------------------- Datenaufbereitung (Scandaten Visualisieren) -----------------------------------
        # CALLBACK 4: Vogelperspektive 
        @self.app.callback(
            Output("birdseye-map", "figure"),
            [Input("scan-df-store", "data"),
             Input("tabs", "active_tab")]
        )
        def update_birdseye_map(scan_data, active_tab):
            if active_tab != "scan":
                return no_update
            if not scan_data:
                return create_birdseye_map(df=None)  # sonst nur Arbeitsbereich einzeichnen
            df = pd.DataFrame(scan_data)
            fig = create_birdseye_map(df[["id", "X", "Y", "Objektart"]])
            return fig
        
        # CALLBACK 5: DataTable mit Scanergebnissen
        @self.app.callback(
            Output("scan-results-container", "children"),
            [Input("scan-df-store", "data"),
             Input("tabs", "active_tab")]
        )
        def update_datatable(scan_data, active_tab):
            if active_tab != "scan":
                return no_update
            if not scan_data:
                return "Keine Scan-Daten oder Objekte im Arbeitsbereich vorhanden."
            df = pd.DataFrame(scan_data)
            return generate_table(df)

        # CALLBACK 6: Dropdowns der Pick&Place befüllen
        @self.app.callback(
            [Output("placement-dropdown-1", "options"),
            Output("placement-dropdown-2", "options"),
            Output("placement-dropdown-single", "options")],
            [Input("scan-df-store", "data"),
             Input("tabs", "active_tab")]
        )
        def update_placement_options(scan_data, active_tab):
            if active_tab != "scan":
                return no_update
            if not scan_data:
                return [[], [], []]
            df = pd.DataFrame(scan_data)
            options = [{"label": f"{row['id']} - {row['Objektart']}", "value": str(row["id"])} 
                    for index, row in df.iterrows()]
            return options, options, options

        # CALLBACK 7: Scan-Bilder im 9x9 Raster
        @self.app.callback(
            Output("scan-images-container", "children"),
            Input("refresh-scan-images", "n_clicks")
        )
        def update_scan_images(n):
            scan_folder = "Scans/makro"
            
            # Finde alle Bilddateien (.png)
            files = sorted([f for f in os.listdir(scan_folder) if f.lower().endswith(('.png'))])
            
            items = []
            total = len(files)
            for i, filename in enumerate(files):
                file_path = os.path.join(scan_folder, filename)
                try:
                    with open(file_path, "rb") as f:
                        encoded = base64.b64encode(f.read()).decode('ascii')
                    src = f"data:image/png;base64,{encoded}"
                    # Erstelle ein Carousel-Item
                    caption = f"Scan-Bild {i+1}/{total}"
                    items.append({
                        "key": filename,
                        "src": src,
                        "header": "",      # Keine Überschrift
                        "caption": caption,     # Beschreibung Bild {x/total}
                        "img_style": {
                            "width": "100%",
                            "height": "auto",
                            "objectFit": "cover"
                        }
                    })
                except Exception as e:
                    continue

            if not items:
                return "Keine Scan-Bilder gefunden."

            carousel = dbc.Carousel(
                items=items,
                controls=True,      # Pfeile zum Navigieren
                indicators=True,    # kleine "Striche" als Indikatoren
                interval=0,         # keine automatische Umschaltung
                ride="carousel",
                style={"width": "100%","height": "auto","margin": "auto"}
            )
            return carousel


        # --------------------------------- SCAN + PICK & PLACE -----------------------------------
        @self.app.callback(
            [
            Output("scan-df-store", "data"),
            Output("placement-status", "children"),
            Output("scan-action-status", "children")
            ],
            [
            Input("btn-scan", "n_clicks"),
            Input("btn-place-objects-compare", "n_clicks"),
            Input("btn-place-object-coord", "n_clicks")
            ],
            [
            State("yolo-dropdown", "value"),
            State("scan-df-store", "data"),
            # Werte aus Sprachbefehl
            State("global-placement-dropdown-1", "value"),
            State("global-placement-dropdown-2", "value"),
            State("global-placement-dropdown-single", "value"),
            State("global-x-coord", "data"),
            State("global-y-coord", "data"),
            # Werte aus Dropdownmenü
            State("placement-dropdown-1", "value"),
            State("placement-dropdown-2", "value"),
            State("placement-dropdown-single", "value"),
            State("placement-x", "value"),
            State("placement-y", "value")
            ]
        )
        def combined_callback(n_scan, n_place_obj, n_place_coord,
                            selected_yolo_model, scan_data,
                            global_dropdown1, global_dropdown2, global_dropdown_single, global_x, global_y,
                            placement_dropdown1, placement_dropdown2, placement_dropdown_single, 
                            placement_x, placement_y):
            """
            Haupt-Callback zur Steuerung des Scan- und Pick-&-Place-Prozesses.

            - Führt den Scan durch, wenn der Scan-Button gedrückt wird.
            - Führt Pick-&-Place-Operationen aus (Objekt zu Objekt oder Objekt zu Koordinaten).

            Args:
                n_scan (int): Anzahl der Klicks auf den Scan-Button.
                n_place_obj (int): Anzahl der Klicks auf den "Platzieren zu Objekt"-Button.
                n_place_coord (int): Anzahl der Klicks auf den "Platzieren zu Koordinaten"-Button.
                selected_yolo_model (str): Aktuell gewähltes YOLO-Modell.
                scan_data (list): Liste der gescannten Objekte.
                global_dropdown1, global_dropdown2, global_dropdown_single (str): Sprachsteuerungs-IDs für die Objektauswahl.
                global_x, global_y (float): Sprachsteuerungs-Koordinaten.
                placement_dropdown1, placement_dropdown2, placement_dropdown_single (str): Manuell gewählte Objektauswahl.
                placement_x, placement_y (float): Manuell eingegebene Koordinaten.

            Returns:
                Tuple:
                    - Aktualisierte Scan-Daten.
                    - Statusmeldung für Pick-&-Place.
                    - Statusmeldung für den Scan-Vorgang.
            """
            
            ctx = callback_context
            if not ctx.triggered:
                return no_update, no_update, no_update
            triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

            # Prüfung Roboterverbindung
            if not (self.qarm and self.qarm.my_arm):
                    return no_update, "Fehler: Roboter nicht korrekt verbunden.", no_update
            
            # ==================== SCAN ====================
            if triggered_id == "btn-scan" and (n_scan is None or n_scan <= 0):
                return no_update, no_update, no_update
            if triggered_id == "btn-scan":
                if not selected_yolo_model:
                    return None, "Kein YOLO Modell ausgewählt. Bitte Modell nutzen.", no_update
                
                scan_manager = ScanManager(
                    yolo_model_path=selected_yolo_model,
                    qarm=self.qarm,
                    camera=self.camera,
                    mysql_manager=self.mysql_manager
                )
                df = scan_manager.run_scan()
                if df.empty:
                    return None, "Keine Objekte erkannt.", no_update
                new_data = df.to_dict('records')
                return new_data, "", "Scan abgeschlossen!"


            # ==================== PICK&PLACE FUNKTIONEN ====================
            
            """Prüfen ob nach Sprachbefehl oder Manuelle Eingabe"""
            # Standardwerte für nicht gesetzte Werte des Sprachbefehls 
            default_dropdown = "-1"
            default_coord = 0.0
            # Bestimme effektive Dropdown-Werte:  Sprachfkt (falls gesetzt); sonst manuell Eingabe 
            effective_dropdown1 = global_dropdown1 if (global_dropdown1 is not None and global_dropdown1 != default_dropdown) else placement_dropdown1
            effective_dropdown2 = global_dropdown2 if (global_dropdown2 is not None and global_dropdown2 != default_dropdown) else placement_dropdown2
            effective_dropdown_single = global_dropdown_single if (global_dropdown_single is not None and global_dropdown_single != default_dropdown) else placement_dropdown_single
            # Bestimme effektive Koordinaten: Sprachfkt (falls gesetzt); sonst manuelle Eingabe
            effective_x = global_x if (global_x is not None and global_x != default_coord) else placement_x
            effective_y = global_y if (global_y is not None and global_y != default_coord) else placement_y


            # ==================== VAR 1 - Objekt zu Objekt ====================
            if triggered_id == "btn-place-objects-compare":
                if not scan_data:
                    return no_update, "Keine Scan-Daten vorhanden.", no_update
                if effective_dropdown1 is None or effective_dropdown2 is None:
                    return scan_data, "Bitte wählen Sie beide Objekte aus.", no_update
                # prüfen ob ids überhaupt möglich in df
                found_obj1 = any(str(row["id"]) == str(effective_dropdown1) for row in scan_data)
                found_obj2 = any(str(row["id"]) == str(effective_dropdown2) for row in scan_data)
                if not (found_obj1 and found_obj2):
                    return scan_data, "Die angegebenen Objekt-IDs liegen außerhalb des verfügbaren Bereichs.", no_update
                self.qarm.gripper(cmd=0)
                coord_a = None
                for row in scan_data:
                    if str(row["id"]) == str(effective_dropdown1):
                        coord_a = [row["X"], row["Y"], 0.05]
                        coord_a1 = [row["X"], row["Y"], 0.15]
                        break
                if coord_a is None:
                    return scan_data, f"Objekt {effective_dropdown1} nicht gefunden.", no_update
                self.qarm.go_to(coord_a)
                self.qarm.gripper(cmd=1) 
                self.qarm.go_to(coord_a1)
                coord_b = None
                for row in scan_data:
                    if str(row["id"]) == str(effective_dropdown2):
                        coord_b0 = [row["X"], row["Y"], 0.15]
                        coord_b = [row["X"], row["Y"], 0.075]
                        break
                if coord_b is None:
                    return scan_data, f"Objekt {effective_dropdown2} nicht gefunden.", no_update
                self.qarm.go_to(coord_b)
                self.qarm.gripper(cmd=0)
                self.qarm.go_to("home")
                for row in scan_data:
                    if str(row["id"]) == str(effective_dropdown1):
                        row["X"] = coord_b[0]
                        row["Y"] = coord_b[1]
                        break
                status_msg = f"Platzierung von Objekt {effective_dropdown1} zu Objekt {effective_dropdown2} durchgeführt."
                return scan_data, status_msg, no_update


            # ==================== VAR 2 - Objekt zu Koord ====================
            elif triggered_id == "btn-place-object-coord":
                if not scan_data:
                    return no_update, "Keine Scan-Daten vorhanden.", no_update
                if effective_dropdown_single is None or (effective_x is None or effective_y is None):
                    return scan_data, "Bitte wählen Sie ein Objekt und geben Sie gültige Koordinaten ein.", no_update
                # prüfen ob id in df erreichbar
                found_obj = any(str(row["id"]) == str(effective_dropdown_single) for row in scan_data)
                if not found_obj:
                    return scan_data, f"Objekt {effective_dropdown_single} nicht gefunden.", no_update
                self.qarm.gripper(cmd=0)
                coord_a = None
                for row in scan_data:
                    if str(row["id"]) == str(effective_dropdown_single):
                        coord_a = [row["X"], row["Y"], 0.05]
                        coord_a1 = [row["X"], row["Y"], 0.15]
                        break
                if coord_a is None:
                    return scan_data, f"Objekt {effective_dropdown_single} nicht gefunden.", no_update
                self.qarm.go_to(coord_a)
                self.qarm.gripper(cmd=1)
                target_coord_0 = [effective_x, effective_y, 0.15]
                self.qarm.go_to(target_coord_0)
                target_coord = [effective_x, effective_y, 0.05]
                self.qarm.go_to(target_coord)
                self.qarm.gripper(cmd=0)
                self.qarm.go_to("home")
                for row in scan_data:
                    if str(row["id"]) == str(effective_dropdown_single):
                        row["X"] = target_coord[0]
                        row["Y"] = target_coord[1]
                        break
                status_msg = f"Platzierung von Objekt {effective_dropdown_single} zu Koordinaten X={effective_x}, Y={effective_y} durchgeführt."
                return scan_data, status_msg, no_update

            else:
                return no_update, no_update, no_update



        # --------------------------------- DataTable erzeugen -----------------------------------
        def generate_table(df):
            """
            Erstellt eine formatierte DataTable zur Anzeige der Scan-Ergebnisse.

            Die Tabelle enthält:
            - Eine dynamische Seitengröße (maximal 10 Einträge pro Seite).
            - Sortier- und Filtermöglichkeiten für die Spalten.
            - Angepasste Zellbreiten und Hintergrundfarben für relevante Spalten.
            - Eine visuell hervorgehobene Kopfzeile mit blauer Hintergrundfarbe.

            Args:
                df (pd.DataFrame): Das Pandas DataFrame mit den Scan-Daten.

            Returns:
                dash_table.DataTable: Dash DataTable mit den formatierten Scan-Daten.
            """
            return dash_table.DataTable(
                data=df.to_dict('records'), # braucht dict-Format
                columns=[{"name": col, "id": col} for col in df.columns],
                page_size=10, # max. Seitenanzahl
                sort_action="native",
                filter_action="native",
                style_table={"overflowX": "auto"},
                style_cell={
                    "textAlign": "center",
                    "color": "black",
                    "padding": "5px",
                    "whiteSpace": "normal",
                    "height": "auto",
                    "border": "1px solid #ccc"
                },
                style_header={
                    "backgroundColor": "#0074D9", # Dunkelblau
                    "fontWeight": "bold",
                    "color": "white",
                    "border": "1px solid #ccc",
                    "textAlign": "center"
                },
                style_cell_conditional=[
                    {"if": {"column_id": "id"}, "width": "10px"},
                    {"if": {"column_id": "Image"}, "width": "100px"},
                    {"if": {"column_id": "X"}, "width": "60px", "backgroundColor": "#87CEFA"}, # Blau
                    {"if": {"column_id": "Y"}, "width": "60px", "backgroundColor": "#87CEFA"},
                    {"if": {"column_id": "Z"}, "width": "60px", "backgroundColor": "#87CEFA"},
                    {"if": {"column_id": "Y1"}, "width": "60px", "backgroundColor": "#FFD700"}, # Gold
                    {"if": {"column_id": "Y2"}, "width": "60px", "backgroundColor": "#FFD700"},
                    {"if": {"column_id": "Y3"}, "width": "60px", "backgroundColor": "#FFD700"},
                    {"if": {"column_id": "Y4"}, "width": "60px", "backgroundColor": "#FFD700"},
                    {"if": {"column_id": "Y5"}, "width": "60px", "backgroundColor": "#FFD700"},
                    {"if": {"column_id": "Objektart"}, "width": "100px"},
                    {"if": {"column_id": "Confidence"}, "width": "150px"},
                    {"if": {"column_id": "Bild_Pfad"}, "width": "300px"}
                ],
                style_filter={"color": "black"} # Schwarzer Text
            )

