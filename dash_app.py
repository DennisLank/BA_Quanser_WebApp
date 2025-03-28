import cv2, dash, os
from dash import dcc, html, Input, Output, State, no_update
import dash_bootstrap_components as dbc
from flask import Response
import numpy as np
import pyrealsense2 as rs


# NavigationBar und Tabs
from navbar import NavBar
from tab_dashboard import Dashboard
from tab_manual_control import ManualControl
from tab_live_feed import LiveFeed
from tab_scan import Scan
from tab_yolo import YoloModel

# Datenbank, Modellverwaltung, Kamera-, Robotersteuerung und STT/TTS
from sql_manager import MySQLManager
from yolo_model import YOLOModelController
from camera import Camera
from QArmControl import QArmControl
import stt_callbacks

# Dash-App erstellen
external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets, 
                suppress_callback_exceptions=True)
server = app.server
app.title = "Quanser 4-DOF Steuerungsdashboard"

# Instanziierung der Modulklassen
yolo_controller = YOLOModelController(app)
sql_manager = MySQLManager()
camera = Camera()
qarm = QArmControl()

# Instanzen für die einzelnen Tabs und Navigation
navbar = NavBar()
dashboard = Dashboard()
manual_control = ManualControl(app=app, qarm=qarm)
live_feed = LiveFeed(app=app, camera=camera)
scan = Scan(app=app, qarm=qarm, camera=camera, mysql_manager=sql_manager)
yolo_tab = YoloModel(app=app, qarm=qarm, camera=camera)

# App Layout
app.layout = html.Div([
    navbar.layout,
    dbc.Tabs(
        id="tabs",
        active_tab="dashboard",
        children=[
            dbc.Tab(label="Dashboard", tab_id="dashboard"),
            dbc.Tab(label="Manuelle Kontrolle", tab_id="manual_control"),
            dbc.Tab(label="Live-Feed", tab_id="live_feed"),
            dbc.Tab(label="Scan", tab_id="scan"),
            dbc.Tab(label="YOLO-Modell", tab_id="yolo_tab"),
        ]
    ),
    html.Div(id="tab-content", style={"padding": "20px"}),

    # Check Verbindungs-Status alle 3s
    # auf System anpassen! --> schauen ob Toast-Pop-Up feuern kann (genug zeit hat)
    dcc.Interval(id="update-setting-icons", interval=3000, n_intervals=0),


    # Speichern von Variablen für die gesamte Session
    dcc.Store(id="scan-df-store", storage_type="session", data=[]), # --> Scan-DataFrame mit allen erkannten Objekten
    dcc.Store(id="stt-command-store", storage_type="session", data=""), # --> STT Befehl
    dcc.Store(id="stt-feedback-store", storage_type="session", data=""), # --> TTS Antwort
    dcc.Store(id="pseudo-click-store", storage_type="session", data=""), # --> Pseudo Klick durch Sprachbefehl
    dcc.Store(id="stt-active-store", storage_type="session", data=False), # --> Mic-Icon einfärben (bis feedback generiert wurde)
        
    # Verbindungszustände
    dcc.Store(id="cam-connection-store", storage_type="session", data=None),
    dcc.Store(id="robot-connection-store", storage_type="session", data=None),

    # Placements Dropdowns aus dem Scan-Tab --> damit kein Error geschmissen wird (Nicht sichtbar)
    html.Div([
        dcc.Dropdown(id="global-placement-dropdown-1", style={"display": "none"}),
        dcc.Dropdown(id="global-placement-dropdown-2", style={"display": "none"}),
        dcc.Dropdown(id="global-placement-dropdown-single", style={"display": "none"}),
        dcc.Store(id="global-x-coord", storage_type="session", data=0.0),
        dcc.Store(id="global-y-coord", storage_type="session", data=0.0),
    ], style={"display": "none"}),

    # Toast-Pop-Ups (Verbindungs- und Statusmeldungen)
    html.Div(
        [
            dbc.Toast(
                id="cam-toast",
                header="Kamera",
                icon="warning",
                duration=4000,
                is_open=False,
                dismissable=True,
                style={"width": "350px"}
            ),
            dbc.Toast(
                id="robot-toast",
                header="Roboter",
                icon="warning",
                duration=4000,
                is_open=False,
                dismissable=True,
                style={"width": "350px"}
            ),
            dbc.Toast(
                id="stt-toast",
                header="Sprachbefehl",
                icon="info",
                duration=4000,
                is_open=False,
                dismissable=True,
                style={"width": "350px"}
            ),
            dbc.Toast(
                id="mic-toast",
                header="Mikrofon",
                icon="info",
                duration=2000,
                is_open=False,
                dismissable=True,
                style={"width": "350px"}
            )
        ],
        id="toast-container",
        style={"position": "fixed", "top": "70px", "right": "10px", "zIndex": 1050,
               "display": "flex", "flexDirection": "column", "alignItems": "flex-end", "gap": "10px"}
    ),

    # Not-Aus Popup und Statusspeicher
    html.Div(id="notaus-status"), 
    dcc.Store(id="notaus-status-store", storage_type="session", data=False),
    html.Div(id="dummy-output", style={"display": "none"}),
    html.Div(id="dummy-output-pseudo-klick", style={"display": "none"})
])
#---------------------------------------------------------------------------------------------------
#-------------------------- LIVE FEED - VIDEO STREAM -----------------------------------------------
#---------------------------------------------------------------------------------------------------
def gen_frames_rgb():
    """Generator, der kontinuierlich den aktuellen RGB-Frame abruft und als MJPEG-Stream liefert."""
    while True:
        # Hole den aktuellen Frame aus dem gemeinsamen Kamera-Puffer
        color_frame, _ = camera.get_stream()
        if color_frame is None:
            continue
        ret, buffer = cv2.imencode('.jpg', color_frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def gen_frames_depth():
    """Generator, der den Tiefenframe (mit Colorizer) abruft und als MJPEG-Stream liefert."""
    colorizer = rs.colorizer()
    while True:
        raw_depth = camera.get_depth_frame_raw()
        if raw_depth is None:
            continue
        try:
            # Wende den Colorizer auf den rohen depth_frame an
            colorized_depth = colorizer.colorize(raw_depth)
        except Exception as e:
            print(f"[FEHLER] Fehler beim Colorisieren des Tiefenframes: {e}")
            continue
        depth_image = np.asanyarray(colorized_depth.get_data())
        ret, buffer = cv2.imencode('.jpg', depth_image)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


# Flask-Routen für die Video-Feeds
@server.route('/video_feed_rgb')
def video_feed_rgb():
    if not camera.check_connection():
        return Response("Keine Kamera verbunden.", mimetype="text/plain")
    return Response(gen_frames_rgb(), mimetype='multipart/x-mixed-replace; boundary=frame')

@server.route('/video_feed_depth')
def video_feed_depth():
    if not camera.check_connection():
        return Response("Keine Kamera verbunden.", mimetype="text/plain")
    return Response(gen_frames_depth(), mimetype='multipart/x-mixed-replace; boundary=frame')

#---------------------------------------------------------------------------------------------------
#------------- TAB-INHALT basierend auf aktivem Tab anzeigen ---------------------------------------
#---------------------------------------------------------------------------------------------------
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab")
)
def render_tab_content(tab):
    if tab == "dashboard":
        return dashboard.layout
    elif tab == "manual_control":
        return manual_control.layout
    elif tab == "live_feed":
        return live_feed.layout
    elif tab == "scan":
        return scan.layout
    elif tab == "yolo_tab":
        return yolo_tab.layout

#---------------------------------------------------------------------------------------------------
#------------------------- Dynamische Icons (Statusanzeigen) ---------------------------------------
#---------------------------------------------------------------------------------------------------
# Datenbank-Icon
@app.callback(
    Output("db-icon", "className"),
    [Input("update-setting-icons", "n_intervals"),
     Input("db-click", "n_clicks")]
)
def update_db_icon(n_intervals, n_clicks):
    ctx = dash.callback_context
    if ctx.triggered:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        # Wenn der Klick-Input (db-click) den Callback auslöst, wird die Verbindung getoggelt
        if trigger_id == "db-click":
            if sql_manager.check_connection():
                print("[INFO] Trenne SQL-Verbindung auf Benutzereingabe...")
                sql_manager.close_connection()
            else:
                print("[INFO] SQL-Verbindung wird aufgebaut...")
                sql_manager.connect()
    # Anschließend wird der aktuelle Status zurückgegeben:
    if sql_manager.check_connection():
        icon_farbe = "connected"
    else:
        icon_farbe = "disconnected"
    return icon_farbe

#---------------------------------------------
# Kamera-Icon
@app.callback(
    [Output("cam-icon", "className"),
     Output("cam-connection-store", "data")],
    [Input("update-setting-icons", "n_intervals"),
     Input("cam-click", "n_clicks")]
)
def update_cam_icon(n_intervals, n_clicks):
    success = None
    ctx = dash.callback_context
    if ctx.triggered:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if trigger_id == "cam-click":
            if camera.check_connection():
                print("[INFO] Kamera-Verbindung wird per Klick getrennt...")
                camera.close_connection()
            else:
                print("[INFO] Kamera-Verbindung wird per Klick hergestellt...")
                success = camera.connect()
    # Icon-Status je Zustand
    if camera.check_connection():
        icon_farbe = "connected"
    else:
        icon_farbe = "disconnected"
    return icon_farbe, success

#---------------------------------------------
# Roboter-Icon
@app.callback(
    [Output("robot-icon", "className"),
     Output("robot-connection-store", "data")],
    [Input("update-setting-icons", "n_intervals"),
     Input("robot-click", "n_clicks")]
)
def update_robot_icon(n_intervals, n_clicks):
    success = None
    ctx = dash.callback_context
    if ctx.triggered:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if trigger_id == "robot-click":
            if qarm.check_connection():
                print("[INFO] Roboter-Verbindung wird per Klick getrennt...")
                qarm.close_connection()
            else:
                print("[INFO] Roboter-Verbindung wird per Klick hergestellt...")
                success = qarm.connect()
    if qarm.check_connection():
        icon_farbe = "connected"
    else:
        icon_farbe = "disconnected"
    return icon_farbe, success

#---------------------------------------------
# Gear-Icon (rot/gelb/grün --> basierend auf den Subsystemen)
@app.callback(
    Output("gear-icon", "className"),
    [Input("db-icon", "className"),
     Input("cam-icon", "className"),
     Input("robot-icon", "className")]
)
def update_gear_icon(db_status, cam_status, robot_status):
    """
    Setzt die Farbe des Zahnrad-Icons:
    - Rot, wenn kein Subsystem verbunden ist.
    - Gelb, wenn mind. ein Subsystem ist.
    - Grün, wenn alle Subsysteme verbunden sind.
    """
    statuses = [db_status, cam_status, robot_status]
    connected_count = statuses.count("connected")
    if connected_count == 3:
        return "connected"
    elif connected_count == 0:
        return "disconnected"
    else:
        return "half_conn"
    
# ------------------------------------------------------
# ------ Toast Benachrichtigungen - Kamera/Roboter -----
# Pop-Up Nachricht ob erfolgreich verbunden wurde
# Kamera
@app.callback(
    [Output("cam-toast", "is_open"),
     Output("cam-toast", "children"),
     Output("cam-toast", "icon")],
    [Input("cam-connection-store", "data")]
)
def show_cam_toast(connection_success):
    """Toast-Pop-Up Benachrichtigung ob die Kamera erfolgreich verbunden wurde."""
    if connection_success is None:
        return no_update, no_update, no_update
    if connection_success:
        return True, "Kamera erfolgreich verbunden.", "success"
    else:
        return True, ["Kamera konnte nicht verbunden werden.",html.Br(),"Bitte USB-Verbindung aus- und wieder einstecken."], "danger"

# Roboter
@app.callback(
    [Output("robot-toast", "is_open"),
     Output("robot-toast", "children"),
     Output("robot-toast", "icon")],
    [Input("robot-connection-store", "data")]
)
def show_robot_toast(connection_success):
    """Toast-Pop-Up Benachrichtigung ob der Roboter erfolgreich verbunden wurde."""
    if connection_success is None:
        return no_update, no_update, no_update
    if connection_success:
        return True, "Roboter erfolgreich verbunden.", "success"
    else:
        return True, ["Roboter konnte nicht verbunden werden.",html.Br(),"Bitte USB-Verbindung aus- und wieder einstecken."], "danger"


#---------------------------------------------------------------------------------------------------
#----------------------------- Sprachbefehl (TTS und STT) ------------------------------------------
#---------------------------------------------------------------------------------------------------
@app.callback(
    Output("mic-click", "style"),
    Input("gear-icon", "className")
)
def update_mic_click_style(gear_class):
    """
    Erlaubt das Anklicken des Mikrofons nur, wenn alle Geräte verbunden sind.
    """
    if gear_class == "connected":
        return {"cursor": "pointer", "pointerEvents": "auto"}
    else:
        return {"cursor": "not-allowed", "pointerEvents": "none"}

@app.callback(
    Output("mic-icon", "className"),
    [Input("gear-icon", "className"),
     Input("stt-active-store", "data")]
)
def update_mic_icon(gear_class, stt_active):
    """
    Setzt die Farbe des Mikrofons:
    - Grau, wenn nicht alle Geräte verbunden sind.
    - Grün, wenn Sprachaufnahme aktiv ist.
    - Gelb im Standby-Modus.
    """
    if gear_class != "connected":
        return "not_available"
    if stt_active:
        return "connected"
    return "half_conn"

# Mic-Icon grün solange Sprachbefehl aufgenommen wird
@app.callback(
    Output("stt-active-store", "data", allow_duplicate=True),
    Input("mic-click", "n_clicks"),
    prevent_initial_call='initial_duplicate'
)
def set_stt_active(n_clicks):
    """Mic-Icon bei klick grün einfärben."""
    if n_clicks:
        return True
    return False
@app.callback(
    Output("stt-active-store", "data", allow_duplicate=True),
    Input("stt-feedback-store", "data"),
    prevent_initial_call='initial_duplicate'
)
def clear_stt_active(_):
    """Mic-Icon wieder auf gelb setzen, wenn Feedback generiert wurde."""
    return False


@app.callback(
    Output("stt-command-store", "data"),
    Input("mic-click", "n_clicks")
)
def trigger_stt(n_clicks):
    """Sprachbefehl aufnehmen, wenn Mic-Icon angeklickt wird."""
    if n_clicks:
        # Sprachbefehl aufnehmen und zrkgeben
        command = stt_callbacks.listen_command()
        return command
    return ""

@app.callback(
    [Output("mic-toast", "is_open"),
     Output("mic-toast", "children")],
    Input("mic-click", "n_clicks")
)
def show_mic_toast(n_clicks):
    """Zeigt ein Toast-Pop-Up an, wenn die Sprachaufnahme gestartet wird."""
    if n_clicks:
        return True, "Aufnahme startet - bitte sprechen..."
    return False, ""

#-------------------------------
# Verarbeitung STT
@app.callback(
    [Output("stt-feedback-store", "data"),
     Output("tabs", "active_tab"),
     Output("pseudo-click-store", "data"),
     Output("global-placement-dropdown-1", "value"),
     Output("global-placement-dropdown-2", "value"),
     Output("global-placement-dropdown-single", "value"),
     Output("global-x-coord", "data"),
     Output("global-y-coord", "data")],
    Input("stt-command-store", "data"),
    State("tabs", "active_tab")
)
def process_stt(command, current_tab):
    """Verarbeitet den erfassten Sprachbefehl."""
    default_val = "-1"
    if command:
        import stt_callbacks
        result = stt_callbacks.process_stt_command(command, qarm)
        feedback = result.get("feedback", "")
        new_tab = result.get("tab") or dash.no_update
        if new_tab == current_tab:
            new_tab = dash.no_update
        simulate_click = result.get("simulate_click") or dash.no_update
        dropdown1 = result.get("set_dropdown1", default_val)
        dropdown2 = result.get("set_dropdown2", default_val)
        dropdown_single = result.get("set_dropdown_single", default_val)
        x_coord = result.get("x_coord", 0.0)
        y_coord = result.get("y_coord", 0.0)
        return feedback, new_tab, simulate_click, dropdown1, dropdown2, dropdown_single, x_coord, y_coord
    return dash.no_update, dash.no_update, dash.no_update, default_val, default_val, default_val, 0.0, 0.0
# Pseudo Klick ausführen
app.clientside_callback(
    """
    function(simulate_click) {
        if(simulate_click && simulate_click !== "") {
            setTimeout(function(){
                var btn = document.getElementById(simulate_click);
                if(btn){
                    btn.click();
                }
            }, 1000);
        }
        return "";
    }
    """,
    Output("dummy-output-pseudo-klick", "children"),
    Input("pseudo-click-store", "data")
)

#-------------------------------
# TOAST Anzeige - Feedback
@app.callback(
    [Output("stt-toast", "is_open"),
     Output("stt-toast", "children")],
    Input("stt-feedback-store", "data")
)
def update_stt_toast(feedback):
    """Toast Benachrichtigung mit dem Feedback zum Sprachbefehl."""
    if feedback:
        return True, feedback
    return False, ""

#---------------------------------------------------------------------------------------------------
#----------------------------- NOTAUS - alle Systeme SOFORT beenden --------------------------------
#---------------------------------------------------------------------------------------------------
@app.callback(
    [Output("notaus-status", "children"),
     Output("notaus-status-store", "data")],
    Input("notaus-button", "n_clicks")
)
def emergency_stop(n_clicks):
    """Aktiviert den Not-Aus und zeigt eine vollflächige Benachrichtigung an."""
    if n_clicks:
        message = html.Div(
            dcc.Markdown("**-- NOT-AUS AKTIVIERT --**  \n**-- APP NEUSTART NOTWENDIG --**"),
            style={
                "position": "fixed", "top": "0", "left": "0", "width": "100%", "height": "100%",
                "backgroundColor": "rgba(255, 0, 0, 0.9)", "color": "white", "fontSize": "50px",
                "display": "flex", "alignItems": "center", "justifyContent": "center",
                "zIndex": "9999", "textAlign": "center"
            }
        )
        return message, True
    return no_update, no_update

@app.callback(
    Output("dummy-output", "children"),
    Input("notaus-status-store", "data")
)
def shutdown_on_emergency(status):
    """Bei Not-Aus alles sofort beenden."""
    if status:
        os._exit(0)
    return ""


#--------------APPSTART--------------------
if __name__ == "__main__":
    app.run_server(debug=True)
