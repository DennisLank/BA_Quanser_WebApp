import glob, os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objs as go
from ultralytics import YOLO

class ScanManager:
    """
    Diese Klasse verwaltet den Scan-Prozess mit dem Roboterarm.
    Sie führt eine Erkennung von Objekten im Arbeitsbereich durch, speichert die Daten in einer MySQL-Datenbank
    und bereinigt doppelte Einträge.
    """
    def __init__(self, yolo_model_path, qarm, camera, mysql_manager):
        """
        Initialisiert den ScanManager mit YOLO-Modell, Roboter, Kamera und Datenbankverwaltung.

        Args:
            yolo_model_path (str): Dateiname des YOLO-Modells (innerhalb des Ordners 'YOLO_Modelle').
            qarm (QArmControl): Instanz der QArm-Steuerung.
            camera (Camera): Instanz der Kamerasteuerung.
            mysql_manager (MySQLManager): Instanz des MySQL-Managements.
        """
        self.qarm = qarm
        self.camera = camera
        self.mysql_manager = mysql_manager

        self.camera.load_new_model(yolo_model_path)
        self.detected_objects_positions = []  # Liste für erkannte Objekte
        self.df = None # DataFrame zur Speicherung der Scandaten

    def clear_scan_directories(self):
        """
        Löscht alle gespeicherten Scanbilder aus dem Verzeichnis 'Scans/makro'.
        """
        macro_dir = r"Scans\makro"
        for dir_path in [macro_dir]:
            for f in glob.glob(os.path.join(dir_path, "*")):
                if os.path.isfile(f):
                    os.remove(f)

    def run_scan(self):
        """
        Führt den vollständigen Scanvorgang durch:
        - Setzt den Roboter in die Ausgangsposition
        - Löscht vorherige Scan-Daten aus der Datenbank
        - Führt die 320°-Erkennung durch
        - Speichert erkannte Objekte in der Datenbank
        - Entfernt doppelte Einträge und setzt die IDs zurück
        - Liefert die gescannten Daten als DataFrame zurück

        Returns:
            pd.DataFrame: Tabelle der erkannten Objekte mit Positionen und Metadaten.
        """
        # Roboter in Home-Position bringen und Greifer öffnen
        self.qarm.go_to("home")
        self.qarm.gripper(cmd=0)

        # Vorherige Tabelle in SQL und Scan-Bilder löschen
        try:
            self.mysql_manager.clear_table("objects")
        except Exception as e:
            print(f"[WARNING] Konnte die SQL-Tabelle nicht löschen (evtl. bereits leer): {e}")
        self.clear_scan_directories()

        # Roboter in die Start-Makroposition bewegen
        scan_coord = (0.3, 0.001, 0.175)
        self.qarm.go_to(coord=scan_coord)

        # Liste zum Speichern der Scan-Daten
        detections_data = []

        # Schleife: Roboter dreht sich um seine Basis (von -160° bis +160° in 40°-Schritten)
        for basis_winkel in range(-160, 161, 40):
            print(f"[INFO] Basis wird auf {basis_winkel}° gedreht.")
            self.qarm.basis_drehen(basis_winkel)

            # YOLO-Detektion im aktuellen Sichtfeld
            result = self.camera.detect_objects(
                qarm=self.qarm,
                confidence_threshold=0.825
            )
            if result is None:
                continue
            detections, img_filename, output_path = result

            # Speichern der Objektdaten und in SQL einfügen
            for detection in detections:
                self.detected_objects_positions.append((detection['grasp_point'], detection['class_name']))
                object_data = {
                    "Image": img_filename,
                    "X": round(detection['grasp_point'][0], 5),
                    "Y": round(detection['grasp_point'][1], 5),
                    "Z": 0,  # Da Objekte auf dem Tisch liegen
                    "Y1": round(np.rad2deg(self.qarm.my_arm.measJointPosition[0]), 2),
                    "Y2": round(np.rad2deg(self.qarm.my_arm.measJointPosition[1]), 2),
                    "Y3": round(np.rad2deg(self.qarm.my_arm.measJointPosition[2]), 2),
                    "Y4": round(np.rad2deg(self.qarm.my_arm.measJointPosition[3]), 2),
                    "Y5": round(np.rad2deg(self.qarm.my_arm.measJointPosition[4]), 2),
                    "Objektart": detection['class_name'],
                    "Confidence": 100 * round(detection['confidence'], 4),
                    "Bild_Pfad": output_path
                }
                try:
                    self.mysql_manager.insert_object_data(object_data)
                except Exception as e:
                    print(f"[ERROR] Fehler beim Einfügen von Daten in SQL: {e}")
            print(f"[INFO] Erkannte Objektart: {detection['class_name']}")

        # Doppelte Positionen (innerhalb eines Toleranzbereichs) filtern
        detected_objects_positions_single = []
        duplicate_ids = []
        for idx, item in enumerate(self.detected_objects_positions, start=1):
            if any(np.allclose(item[0][:2], existing[0][:2], atol=0.1) and item[1] == existing[1]
                   for existing in detected_objects_positions_single):
                duplicate_ids.append(idx)
            else:
                detected_objects_positions_single.append(item)

        # Doppelte Einträge in der Datenbank entfernen und IDs zurücksetzen
        if duplicate_ids:
            try:
                self.mysql_manager.remove_duplicates_and_reset_ids(duplicate_ids=duplicate_ids)
            except Exception as e:
                print(f"[ERROR] Fehler beim Entfernen von Duplikaten: {e}")

        # Endgültige Daten aus der SQL-Datenbank abrufen
        try:
            engine = create_engine('mysql+mysqlconnector://root:123SA2@localhost/objects_db')
            with engine.connect() as conn:
                df = pd.read_sql("SELECT * FROM objects;", con=conn)
            self.df = df
        except Exception as e:
            print(f"[ERROR] Fehler beim Abrufen der SQL-Daten: {e}")
            df = pd.DataFrame()  # Leeres DataFrame zurückgeben, falls SQL-Fehler auftritt

        # Scan abschließen: Roboter zurück in Home-Position bringen
        self.qarm.go_to("home")
        print("[INFO] Scan abgeschlossen.")
        return df

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
def create_birdseye_map(df):
    """
    Erzeugt eine 2D-Vogelperspektive als Plotly-Figure basierend auf dem Scan-Ergebnis.
    - Positive X-Werte erscheinen links
    - Positive Y-Werte erscheinen unten
    - Arbeitsbereich des Roboters
    - Achsenbereich +-0.8

    Args:
        df (pd.DataFrame): DataFrame mit (mind.) den Spalten ["id", "X", "Y", "Objektart"].

    Returns:
        go.Figure: Plotly-Objekt der Karte mit Arbeitsbereich und erkannten Objekten.
    """
    radius_max = 0.7536
    radius_min = 0.25
    
    # -----------------------------
    # Arbeitsbereich des Roboters --> grün
    theta_full = np.linspace(0, 2*np.pi, 200)
    x_outer = radius_max * np.cos(theta_full)
    y_outer = radius_max * np.sin(theta_full)
    x_inner = radius_min * np.cos(theta_full[::-1])
    y_inner = radius_min * np.sin(theta_full[::-1])
    x_annulus = np.concatenate([x_outer, x_inner])
    y_annulus = np.concatenate([y_outer, y_inner])
    trace_annulus = go.Scatter(
        x=x_annulus,
        y=y_annulus,
        mode="lines",
        fill="toself",
        fillcolor="lightgreen",
        line=dict(color="lightgreen"),
        name="Arbeitsbereich"
    )
    
    # -----------------------------
    # Randkreise für Reichweite
    trace_circle_max = go.Scatter(
        x=radius_max * np.cos(theta_full),
        y=radius_max * np.sin(theta_full),
        mode="lines",
        line=dict(color="green"),
        name="Max. Reichweite"
    )
    trace_circle_min = go.Scatter(
        x=radius_min * np.cos(theta_full),
        y=radius_min * np.sin(theta_full),
        mode="lines",
        line=dict(color="green"),
        name="Mindestabstand"
    )
    
    # -----------------------------
    # Toter Winkel im Bereich 170° bis 190° --> grau
    dead_min = np.deg2rad(170)
    dead_max = np.deg2rad(190)
    n_points = 50
    theta_wedge = np.linspace(dead_min, dead_max, n_points)
    x_wedge = [0]
    y_wedge = [0]
    for ang in theta_wedge:
        x_wedge.append(radius_max * np.cos(ang))
        y_wedge.append(radius_max * np.sin(ang))
    x_wedge.append(0)
    y_wedge.append(0)
    trace_wedge = go.Scatter(
        x=x_wedge,
        y=y_wedge,
        mode="lines",
        fill="toself",
        fillcolor="lightgray",
        line=dict(color="gray"),
        name="Toter Winkel"
    )

    # Koordinatenkreuz am Ursprung
    # X-Achse nach links
    coord_x = go.Scatter(
        x=[0, 0.2],
        y=[0, 0],
        mode='lines+text',
        line=dict(color='black'),
        text=["", " X"],  # Beschriftung am zweiten Punkt
        textposition='middle left',
        showlegend=False
    )
    # Y-Achse nach unten
    coord_y = go.Scatter(
        x=[0, 0],
        y=[0, 0.2],
        mode='lines+text',
        line=dict(color='black'),
        text=["", " Y"],  # Beschriftung am zweiten Punkt
        textposition='bottom center',
        showlegend=False
    )

    # -----------------------------
    # Objekte aus der Datenbank (falls vorhanden)
    # -----------------------------
    if df is not None and not df.empty:
        trace_objects = go.Scatter(
            x=df["X"],
            y=df["Y"],
            mode="markers+text",
            marker=dict(color="red", size=10),
            text=[str(row["id"]) for index, row in df.iterrows()],  # IDs werden als Text angezeigt
            textposition="top center",
            customdata=df[["id", "Objektart", "X", "Y"]].values,  # zusätzliche Daten beim Hovern über den Punkten
            hovertemplate=(
                "<b>ID:</b> %{customdata[0]}<br>"
                "<b>Objektart:</b> %{customdata[1]}<br>"
                "<b>X:</b> %{customdata[2]:.2f} m<br>"
                "<b>Y:</b> %{customdata[3]:.2f} m<extra></extra>"
            ),
            name="Objekte"
        )
    else:
        trace_objects = go.Scatter(
            x=[], 
            y=[], 
            mode="markers+text", 
            marker=dict(color="red", size=10), 
            name="Objekte"
        )
    
    layout = go.Layout(
        xaxis=dict(
            title="X (in Meter)",
            range=[0.8, -0.8],
            constrain="domain"
        ),
        yaxis=dict(
            title="Y (in Meter)",
            range=[0.8, -0.8],
            scaleanchor="x"
        ),
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
        showlegend=False,
        title=""
    )
    
    fig = go.Figure(
        data=[
            trace_annulus,
            trace_circle_max,
            trace_circle_min,
            trace_wedge,
            trace_objects,
            coord_x,
            coord_y
        ],
        layout=layout
    )
    return fig

