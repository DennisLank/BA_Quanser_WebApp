import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input

class LiveFeed:
    """
    Diese Klasse verwaltet den "Live-Feed"-Tab der Dash-Anwendung.

    Funktionen:
    - Zeigt den Live-Kamerastream des Quanser 4-DOF Roboters an (RGB oder Tiefenbild).
    - Ermöglicht das Umschalten zwischen RGB- und Tiefenbildmodus.
    - Überprüft regelmäßig die Kameraverbindung und aktualisiert den Statusindikator.
    - Bietet die Möglichkeit, den Live-Feed in einem separaten Fenster zu öffnen.
    """
    def __init__(self, app, camera):
        """
        Initialisiert die Live-Feed-Klasse.

        Args:
            :param app: Die Dash-App-Instanz, in die die Callbacks registriert werden.
            :param camera: Eine Instanz der Kamera-Klasse, die Methoden wie start_camera(), stop() 
                        und check_connection() bereitstellt.
        """
        self.app = app
        self.camera = camera
        self.layout = self.render_layout()
        self.register_callbacks()

    def render_layout(self):
        """
        Erstellt das Layout für den "Roboter Live-Feed"-Tab.
        
        Enthält:
        - Live-Indikator zur Anzeige der Kameraverbindung.
        - Schalter zum Wechsel zwischen RGB- und Tiefenbild.
        - Bereich zur Anzeige des Kamerastreams.
        - Buttons zum Öffnen des Feeds in separaten Fenstern.
        - Unsichtbare Dummy-Divs für die Client-Callbacks.

        Returns:
            html.Div: Layout für den Live-Feed-Tab.
        """
        return dbc.Row([
            dbc.Col([
                dcc.Interval(id="interval-check", interval=1000, n_intervals=0),
                html.H4([
                    "Roboter Live-Feed ",
                    html.Span(id="live-indicator")
                ]),
                dbc.Switch(
                    id="feed-switch",
                    label="RGB/Tiefenbild",
                    value=False,
                    className="mb-3"
                ),
                html.Div(id="feed-container"),

                # Buttons für externe Fenster
                dbc.Button("Extra Fenster: Farbbild", id="btn-extra-farbbild", color="info", className="mt-3"),
                dbc.Button("Extra Fenster: Tiefenbild", id="btn-extra-tiefenbild", color="info", className="mt-3"),
                
                # Unsichtbare Dummy-Divs für die Client-Callbacks
                html.Div(id="dummy-output-farbbild", style={"display": "none"}),
                html.Div(id="dummy-output-tiefenbild", style={"display": "none"})
            ], width=12),
        ])


    def register_callbacks(self):
        """
        Registriert alle Callbacks für den Live-Feed-Tab.
        """

        # Display
        @self.app.callback(
            Output("feed-container", "children"),
            [Input("feed-switch", "value"),
             Input("interval-check", "n_intervals")]
        )
        def update_feed_display(is_depth_on, n_intervals):
            """
            Aktualisiert den Live-Feed-Bereich basierend auf dem gewählten Bildmodus (RGB/Tiefenbild).
            
            Args:
                is_depth_on (bool): Gibt an, ob der Tiefenbildmodus aktiviert ist.
                n_intervals (int): Intervall-Trigger zur regelmäßigen Aktualisierung.

            Returns:
                html.Img oder html.H5: Bild oder Hinweistext bei fehlender Verbindung.
            """
            if not self.camera.check_connection():
                return html.H5("- Kein Signal -", style={"color": "orange"})
            if is_depth_on:
                return html.Img(src="/video_feed_depth", style={"width": "100%"})
            else:
                return html.Img(src="/video_feed_rgb", style={"width": "100%"})

        # Live-Indikator
        @self.app.callback(
            Output("live-indicator", "children"),
            Input("interval-check", "n_intervals")
        )
        def update_live_indicator(n):
            if self.camera.check_connection():
                return html.Span(
                    ["Live", html.Span(className="blinking-dot")],
                    style={"fontWeight": "bold", "color": "red", "marginLeft": "10px"}
                )
            else:
                return html.Span(
                    ["Offline", html.Span(className="dot-offline")],
                    style={"fontWeight": "bold", "color": "grey", "marginLeft": "10px"}
                )
            
        # Clientside Callback: Öffnet ein neues Fenster für das Farbbild
        self.app.clientside_callback(
            """
            function(n_clicks) {
                if(n_clicks > 0) {
                    window.open('/video_feed_rgb', '_blank');
                }
                return "";
            }
            """,
            Output('dummy-output-farbbild', 'children'),
            Input('btn-extra-farbbild', 'n_clicks')
        )

        # Clientside Callback: Öffnet ein neues Fenster für das Tiefenbild
        self.app.clientside_callback(
            """
            function(n_clicks) {
                if(n_clicks > 0) {
                    window.open('/video_feed_depth', '_blank');
                }
                return "";
            }
            """,
            Output('dummy-output-tiefenbild', 'children'),
            Input('btn-extra-tiefenbild', 'n_clicks')
        )
