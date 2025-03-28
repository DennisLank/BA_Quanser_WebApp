import dash_bootstrap_components as dbc
from dash import html, dcc

class NavBar:
    """
    Erstellt die Navigationsleiste für das Quanser 4-DOF Steuerungsdashboard.
    Enthält Statusanzeigen für Roboter, Kamera und Datenbank sowie Steuerungsoptionen.
    """

    def __init__(self):
        """Initialisiert die Navigationsleiste."""
        self.layout = self.create_navbar()

    def create_navbar(self):
        """
        Erstellt die Navbar mit Icons für den Verbindungsstatus, einer YOLO-Modellauswahl,
        einem Mikrofon-Button für Sprachbefehle sowie einem Not-Aus-Button.

        Returns:
            dbc.Navbar: Die vollständige Dash-Navigationsleiste.
        """
        # YOLO-Modell-Auswahl (Dropdown)
        yolo_selector = html.Div([
            html.Label("YOLO:", style={"color": "white", "marginBottom": "0.2rem"}),
            dcc.Dropdown(
                id="yolo-dropdown",
                options=[],       # wird über den Intervall-Callback gefüllt
                value=None,
                placeholder="Modell wählen...",
                clearable=False,
                style={"width": "200px", "color": "black"}   
            )
        ], style={"padding": "0.5rem"})

        # Status-Icons für Roboter, Kamera und Datenbank
        icons_row = dbc.Row(
            [
                dbc.Col(
                    html.A(
                        html.Img(
                            id="robot-icon",
                            src="/assets/icons/robot.svg",
                            className="disconnected",
                            style={"height": "1.5em"}
                        ),
                        id="robot-click",
                        href="#"
                    ),
                    width="auto"
                ),
                dbc.Col(
                    html.A(
                        html.Img(
                            id="cam-icon",
                            src="/assets/icons/camera.svg",
                            className="disconnected",
                            style={"height": "1.5em"}
                        ),
                        id="cam-click",
                        href="#"
                    ),
                    width="auto"
                ),
                dbc.Col(
                    html.A(
                        html.Img(
                            id="db-icon",
                            src="/assets/icons/database.svg",
                            className="disconnected",
                            style={"height": "1.5em"}
                        ),
                        id="db-click",
                        href="#"
                    ),
                    width="auto"
                )
            ],
            justify="around",
            align="center",
            className="mb-2"  # optionaler Abstand nach unten
        )

        # Dropdown-Menü für Einstellungen (enthält Status-Icons und YOLO-Auswahl)
        settings_dropdown = dbc.DropdownMenu(
            children=[
                icons_row,
                dbc.DropdownMenuItem(divider=True),
                html.Div([yolo_selector])
            ],
            nav=True,
            in_navbar=True,
            label=html.Img(
                id="gear-icon",
                src="/assets/icons/gear.svg", 
                style={"height": "1.5em"}
                ),
            toggle_style={"padding": "0.5rem"},
            direction="left"  # öffnet Dropdown nach links
        )

        # Mic-Icon für Sprachsteuerung
        mic_icon = dbc.NavItem(
            html.A(
                html.Img(
                    id="mic-icon",
                    src="/assets/icons/microphone.svg",
                    className = "not_available",
                    style={"height": "1.5em", "cursor": "pointer"}
                ),
                id="mic-click",
                href="#"
            )
        )

        # Not-Aus-Button zentral
        notaus_button = dbc.Button(
            "Not-Aus",
            id="notaus-button",
            color="danger",
            size="lg",
            outline=False,
            style={"fontWeight": "bold", "width": "200px"}
        )


        # Zusammenbau der Navbar
        navbar = dbc.Navbar(
            dbc.Container(
                fluid = True,
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.NavbarBrand("Quanser 4-DOF Robotersteuerung", href="#"),
                                width=3,
                                className="d-flex align-items-center"
                            ),
                            dbc.Col(
                                notaus_button,
                                width=6,
                                className="d-flex justify-content-center align-items-center"
                            ),
                            dbc.Col(
                                dbc.Nav(
                                    [
                                        settings_dropdown,
                                        html.Div(style={"width": "10px"}),  # kleiner Puffer
                                        mic_icon
                                    ],
                                    className="d-flex justify-content-end align-items-center",
                                    navbar=True
                                ),
                                width=3
                            )
                        ],
                        align="center",
                        justify="between",
                        className="w-100"
                    )
                ]
            ),
            color="dark",
            dark=True,
            sticky="top"
        )
        return navbar
