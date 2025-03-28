import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback_context, Output, Input, State, no_update
import numpy as np

class ManualControl:
    """
    Diese Klasse verwaltet den "Manuelle Kontrolle"-Tab der Dash-Anwendung.

    Funktionen:
    - Steuerung des Quanser 4-DOF Roboters über Buttons für Basis, Schulter, Ellbogen und LED.
    - Manuelle Eingabe von XYZ-Koordinaten und Rotation für gezielte Bewegungen.
    - Speicherung des letzten LED-Farbwerts über die gesamte Sitzung.
    - Automatische Aktivierung/Deaktivierung von Buttons je nach Verbindungsstatus.
    """
    def __init__(self, app, qarm):
        """
        Initialisiert die Klasse für die manuelle Robotersteuerung.

        Args:
            :param app: Die Dash-App-Instanz.
            :param robot_obj: Instanz des Roboter-Controllers (QArmControl), 
                            über die Methoden wie LED_Control, go_to und go_to_joint gesteuert werden.
        """
        self.app = app
        self.qarm = qarm
        self.layout = self.render_layout()
        self.register_callbacks()

    def render_layout(self):
        """
        Erstellt das Layout für den "Manuelle Kontrolle"-Tab.

        Enthält:
        - Statusanzeige zur Roboterverbindung.
        - LED-Steuerung mit drei Farben.
        - Manuelle Koordinatensteuerung (XYZ & Rotation).
        - Buttons zur direkten Gelenksteuerung.
        - Speicherung des letzten LED-Farbwerts (Session-Storage).

        Returns:
            dbc.Container: Layout für den manuellen Steuerungs-Tab.
        """
        return dbc.Container([
            # -----------------------------------------
            # Row 1: Einleitung und Roboterstatus
            # -----------------------------------------
            html.H4("Manuelle Kontrolle"),
            html.P("Die Buttons und Funktionen werden freigeschaltet, wenn ein Roboter verbunden ist."),
            html.Div(id="robot-status-message", style={"color": "red", "fontWeight": "bold", "marginBottom": "10px"}),
            html.Hr(),

            # -----------------------------------------
            # Row 2: Links--> Roboterverbindung & LED-Steuerung, Rechts--> Bild des RoboArms
            # -----------------------------------------
            dbc.Row([
                dbc.Col([
                    # LED-Steuerung (Farbpalette)
                    html.H5("LED-Steuerung:"),
                    dbc.ButtonGroup([
                        dbc.Button("", id="btn-led-rot", style={
                            "backgroundColor": "red", "width": "100px", "height": "100px", "marginRight": "10px"
                        }),
                        dbc.Button("", id="btn-led-gruen", style={
                            "backgroundColor": "green", "width": "100px", "height": "100px", "marginRight": "10px"
                        }),
                        dbc.Button("", id="btn-led-blau", style={
                            "backgroundColor": "blue", "width": "100px", "height": "100px", "marginRight": "10px"
                        }),
                    ], className="mb-3"),
                    html.Div(id="led-status", className="mb-3"),
                ], width=6),  # Linke Spalte: 1/2 Breite

                dbc.Col([
                    # Rechts das Bild
                    html.Img(
                        src="/assets/qarm_image.jpg",
                        style={"maxWidth": "100%", "height": "auto"}
                    )
                ], width=6)  # Rechte Spalte: 1/2 Breite
            ]),
            html.Hr(),
            # -----------------------------------------
            # Row 3: Koordinatenfahrt
            # -----------------------------------------
            dbc.Row([
                dbc.Col([
                    html.H5("Koordinatenfahrt:"),
                    dbc.InputGroup([
                        dbc.InputGroupText("X"),
                        dbc.Input(id="coord-x", type="number", placeholder="z.B. 0.5", value=0.5)
                    ], className="mb-2"),
                    dbc.InputGroup([
                        dbc.InputGroupText("Y"),
                        dbc.Input(id="coord-y", type="number", placeholder="z.B. 0.0", value=0.0)
                    ], className="mb-2"),
                    dbc.InputGroup([
                        dbc.InputGroupText("Z"),
                        dbc.Input(id="coord-z", type="number", placeholder="z.B. 0.4", value=0.4)
                    ], className="mb-2"),
                    dbc.InputGroup([
                        dbc.InputGroupText("Rotation (°)"),
                        dbc.Input(id="coord-rot", type="number", placeholder="0", value=0)
                    ], className="mb-2"),
                    dbc.Button("Anfahren", id="btn-go-to-coord", color="primary", className="mb-3"),
                    html.Div(id="coord-status", className="mb-3"),
                ], width=12)
            ]),
            html.Hr(),
            # -----------------------------------------
            # Row 4: Manuelle Gelenksteuerung
            # -----------------------------------------
            dcc.Slider(
                id="step-size-slider",
                min=5,
                max=50,
                marks={5: "5°", 10: "10°", 15: "15°", 20: "20°", 25: "25°", 50: "50°"},
                step=None,
                value=10,  # Standardwert
                tooltip={"placement": "bottom", "always_visible": True},
            ),

            dbc.Row([
                dbc.Col([
                    html.H5("Manuelle Gelenksteuerung:"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Basis nach links", id="btn-base-plus", color="secondary", className="mb-2"),
                            dbc.Button("Basis nach rechts", id="btn-base-minus", color="secondary", className="mb-2")
                        ], width=4),
                        dbc.Col([
                            dbc.Button("Schulter runter", id="btn-shoulder-plus", color="secondary", className="mb-2"),
                            dbc.Button("Schulter hoch", id="btn-shoulder-minus", color="secondary", className="mb-2")
                        ], width=4),
                        dbc.Col([
                            dbc.Button("Ellbogen runter", id="btn-elbow-plus", color="secondary", className="mb-2"),
                            dbc.Button("Ellbogen hoch", id="btn-elbow-minus", color="secondary", className="mb-2")
                        ], width=4),
                    ]),
                    html.Div(id="manual-control-status", className="mt-3")
                ], width=12)
            ]),

            # Solange im Tab --> letzte LED der Basis speichern
            dcc.Store(id="led-color-store", storage_type="session", data=np.array([1, 0, 0], dtype=np.float64)),
        ], fluid=True)


    def register_callbacks(self):
        """Registriert alle Callbacks für die manuelle Steuerung."""

        # ------------------------------------- Statusanzeigen -------------------------------------
        # Statusanzeige - Roboter verbunden oder nicht
        @self.app.callback(
            [Output("robot-status-message", "children"),
             Output("robot-status-message", "style")],
            Input("update-setting-icons", "n_intervals")
        )
        def update_robot_status(n):
            if self.qarm and self.qarm.check_connection():
                return "Roboterstatus: Verbunden", {"color": "green", "fontWeight": "bold", "marginBottom": "10px"}
            else:
                return "Roboterstatus: Nicht verbunden - Bitte verbinden Sie den Roboter, um die Funktionen zu nutzen.", \
                    {"color": "red", "fontWeight": "bold", "marginBottom": "10px"}
                       
        # Deaktivierung der Buttons, solange der Roboter nicht verbunden ist
        @self.app.callback(
            [Output("btn-led-rot", "disabled"),
             Output("btn-led-gruen", "disabled"),
             Output("btn-led-blau", "disabled"),
             Output("btn-go-to-coord", "disabled"),
             Output("btn-base-plus", "disabled"),
             Output("btn-base-minus", "disabled"),
             Output("btn-shoulder-plus", "disabled"),
             Output("btn-shoulder-minus", "disabled"),
             Output("btn-elbow-plus", "disabled"),
             Output("btn-elbow-minus", "disabled")],
            Input("update-setting-icons", "n_intervals")
        )
        def disable_buttons(n_intervals):
            if self.qarm and self.qarm.check_connection():
                # Alle Buttons aktiv
                return [False] * 10
            # Sonst alle deaktivieren
            return [True] * 10

        # ------------------------------------- Funktionen -------------------------------------
        # Callback für LED-Steuerung
        @self.app.callback(
            [Output("led-status", "children"),
             Output("led-color-store", "data")],
            [Input("btn-led-rot", "n_clicks"),
             Input("btn-led-gruen", "n_clicks"),
             Input("btn-led-blau", "n_clicks")]
        )
        def set_led_color(n_rot, n_gruen, n_blau):
            if self.qarm is None or self.qarm.my_arm is None:
                return "Roboter nicht verbunden.", no_update
            
            ctx = callback_context
            if not ctx.triggered:
                return "", no_update
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            if button_id == "btn-led-rot":
                cmd = [1, 0, 0]
                color = "rot"
            elif button_id == "btn-led-gruen":
                cmd = [0, 1, 0]
                color = "grün"
            elif button_id == "btn-led-blau":
                cmd = [0, 0, 1]
                color = "blau"
            else:
                return "", dash.no_update
            self.qarm.LED_Control(np.array(cmd, dtype=np.float64))
            return f"LED auf {color} gesetzt.", cmd

        # Koordinatenfahrt
        @self.app.callback(
            Output("coord-status", "children"),
            Input("btn-go-to-coord", "n_clicks"),
            [State("coord-x", "value"),
             State("coord-y", "value"),
             State("coord-z", "value"),
             State("coord-rot", "value"),
             State("led-color-store", "data")]
        )
        def go_to_coord(n_clicks, x, y, z, rot, led_cmd):
            if n_clicks:
                if self.qarm is None:
                    return "Roboter nicht verbunden."
                if z is None or z < 0.15:
                    return "⚠️ Achtung Tisch! Die z-Koordinate muss mindestens 0.15 sein."
                coord = np.array([x, y, z])
                try:
                    self.qarm.go_to(coord, rotation=rot if rot is not None else 0)
                    self.qarm.LED_Control(np.array(led_cmd, dtype=np.float64))
                    return f"Fahre zu: X={x}, Y={y}, Z={z} (Rotation: {rot if rot is not None else 0}°)."
                except Exception as e:
                    return f"Fehler bei Koordinatenfahrt: {str(e)}"
            return ""

        # Manuelle Gelenksteuerung
        @self.app.callback(
            Output("manual-control-status", "children"),
            [Input("btn-base-plus", "n_clicks"),
             Input("btn-base-minus", "n_clicks"),
             Input("btn-shoulder-plus", "n_clicks"),
             Input("btn-shoulder-minus", "n_clicks"),
             Input("btn-elbow-plus", "n_clicks"),
             Input("btn-elbow-minus", "n_clicks")],
            [State("step-size-slider", "value"),
             State("led-color-store", "data")]
        )
        def manual_joint_control(btn_base_plus, btn_base_minus, btn_shoulder_plus, btn_shoulder_minus, btn_elbow_plus, btn_elbow_minus, step_size, led_cmd):
            ctx = callback_context
            if not ctx.triggered:
                return ""
            if self.qarm is None:
                return "Roboter nicht verbunden."
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            try:
                self.qarm.my_arm.read_std()  # Aktualisiere die aktuellen Gelenkpositionen
                scan_pos_joints = np.copy(self.qarm.my_arm.measJointPosition[:4])
                step_size = step_size if step_size else 5

                if button_id == "btn-base-plus":
                    scan_pos_joints[0] += np.radians(step_size)
                elif button_id == "btn-base-minus":
                    scan_pos_joints[0] -= np.radians(step_size)
                elif button_id == "btn-shoulder-plus":
                    scan_pos_joints[1] += np.radians(step_size)
                elif button_id == "btn-shoulder-minus":
                    scan_pos_joints[1] -= np.radians(step_size)
                elif button_id == "btn-elbow-plus":
                    scan_pos_joints[2] += np.radians(step_size)
                elif button_id == "btn-elbow-minus":
                    scan_pos_joints[2] -= np.radians(step_size)

                self.qarm.go_to_joint(scan_pos_joints)
                self.qarm.LED_Control((np.array(led_cmd, dtype=np.float64)))
                return f"Gelenkbewegung ausgeführt: {np.degrees(scan_pos_joints)}"
            except Exception as e:
                return f"Fehler bei manueller Gelenksteuerung: {str(e)}"







        