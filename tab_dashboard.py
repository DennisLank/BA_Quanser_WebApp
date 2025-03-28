from dash import html, dcc
import dash_bootstrap_components as dbc

class Dashboard:
    def __init__(self):
        self.layout = self.render_layout()

    def render_layout(self):
        return dbc.Container([
            html.H2("Quanser 4-DOF Robotersteuerung", className="mt-4"),
            html.P("Herzlich Willkommen zur webbasierten Steuerung und Überwachung des Quanser 4-DOF Roboters. "
                   "Diese Applikation vereint manuelle und automatische Steuerungsmöglichkeiten, Echtzeitüberwachung sowie den Einsatz "
                   "modernster KI-Modelle zur Objekterkennung und -manipulation."),

            html.Hr(),

            html.H4("Hauptfunktionen des Dashboards:"),
            dbc.ListGroup([
                dbc.ListGroupItem([html.B("Dashboard:"), " Übersicht und Einführung in die Nutzung der webbasierten Applikation."]),
                dbc.ListGroupItem([html.B("Manuelle Kontrolle:"), " Präzise Steuerung des Roboters über Gelenkbewegungen, Koordinatenfahrt und LED-Basissteuerung."]),
                dbc.ListGroupItem([html.B("Roboter Live-Feed:"), " Echtzeitüberwachung des Arbeitsbereichs mittels RGB- und Tiefenkameratechnologie."]),
                dbc.ListGroupItem([html.B("Scan-Funktion:"), " Automatisierte Objekterkennung und -lokalisierung mittels YOLOv11, einschließlich Pick-&-Place-Operationen."]),
                dbc.ListGroupItem([html.B("YOLO-Modellverwaltung:"), " Upload, Verwaltung und Erstellung von Trainingsdatensätzen für neue KI-Modelle zur visuellen Objekterkennung."]),
            ], className="mb-4"),

            html.Div(className="alert alert-info", children=[
                html.B("Hinweis:"),
                " Diese Applikation entstand im Rahmen meiner abgeschlossenen Bachelorarbeit als robuste und wissenschaftlich fundierte Steuerungsplattform. "
                "Trotz umfassender Tests können vereinzelte Fehler unter realen Bedingungen nicht vollständig ausgeschlossen werden und bieten Potenzial für zukünftige Weiterentwicklungen."
            ]),

            html.Hr(),

            html.H4("Systemstatus-Icons und ihre Bedeutung:"),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Icon"), html.Th("Status"), html.Th("Beschreibung")]))
            , html.Tbody([
                html.Tr([html.Td("⚙️ Zahnrad"), html.Td("🔴/🟡/🟢"), html.Td("Gesamtstatus der Subsysteme (Roboter, Kamera, Datenbank).")]),
                html.Tr([html.Td("🤖 Roboter"), html.Td("🔴/🟢"), html.Td("Verbindungsstatus des Roboters; Klick aktiviert/deaktiviert Verbindung.")]),
                html.Tr([html.Td("📷 Kamera"), html.Td("🔴/🟢"), html.Td("Verbindungsstatus der Kamera; Klick aktiviert/deaktiviert Verbindung.")]),
                html.Tr([html.Td("🗄️ Datenbank"), html.Td("🔴/🟢"), html.Td("Verbindungsstatus zum SQL-Server; Klick aktiviert/deaktiviert Verbindung.")]),
                html.Tr([html.Td("🎙️ Mikrofon"), html.Td("🟡/🟢/⚪"), html.Td("Status der Sprachsteuerung: Standby, aktiv oder deaktiviert.")]),
                html.Tr([html.Td("🛑 Not-Aus"), html.Td("🔴"), html.Td("Sofortiges Abschalten aller Prozesse; Neustart erforderlich.")]),
            ])], bordered=True, hover=True),

            html.Hr(),

            html.H4("Verfügbare Sprachbefehle:"),
            html.P("Um folgende Sprachbefehle zur intuitiven Robotersteuerung nutzen zu können, müssen alle Subsysteme verbunden sein. "
                    "Die Aufnahme Ihres Sprachbefehls erfolgt nach einem Klick auf das Mikrofon-Icon."),
            dbc.ListGroup([
                dbc.ListGroupItem(html.Code('"Zur [Home/Start]-Position bewegen" - Roboter zur Home-Position steuern.')),
                dbc.ListGroupItem(html.Code('"Setze RGB auf [rot/grün/blau]" - LED-Farbe einstellen.')),
                dbc.ListGroupItem(html.Code('"Zeige mir das [Farbbild/Tiefenbild]" - Kameramodus wechseln.')),
                dbc.ListGroupItem(html.Code('"Bewege die Basis nach [links/rechts]" - Steuerung des Basisgelenks.')),
                dbc.ListGroupItem(html.Code('"Bewege die Schulter [hoch/runter]" - Steuerung des Schultergelenks.')),
                dbc.ListGroupItem(html.Code('"Bewege den Ellbogen [hoch/runter]" - Steuerung des Ellbogengelenks.')),
                dbc.ListGroupItem(html.Code('"Scan durchführen" - Automatischen Scan des Arbeitsbereiches starten.')),
                dbc.ListGroupItem(html.Code('"Platziere Objekt {id} zu Objekt {id}" - Durchführung einer Pick-&-Place-Operation zwischen Objekten.')),
                dbc.ListGroupItem(html.Code('"Platziere Objekt {id} zu Koordinaten x={x}, y={y}" - Präzise Positionierung eines Objekts an angegebene Koordinaten.')),
            ], className="mb-4"),

            html.Div(className="alert alert-warning", children=[
                html.B("Wichtig:"),
                " Nutzen Sie den Not-Aus-Button nur in Notfällen, da anschließend ein Neustart der Anwendung erforderlich ist."
            ]),

            html.P("Statusmeldungen erscheinen kurzzeitig (2-4 Sek.) als Toast-Pop-ups oben rechts."),

            html.Hr(),

            html.H4("📚 Kontext der Web-Applikation"),
            html.P("Diese Applikation wurde im Rahmen meiner Bachelorarbeit im Studiengang Maschinenbau an der Ostfalia Hochschule für "
            "angewandte Wissenschaften entwickelt. Ziel war die Realisierung einer intuitiven und leistungsfähigen Steuerungsplattform für "
            "den Quanser 4-DOF Roboter, verbunden mit KI-gestützten Verfahren zur Objekterkennung und -manipulation."),

            html.Ul([
                html.Li([html.B("Erstprüfer:"), " Prof. Dr.-Ing. Peter Engel"]),
                html.Li([html.B("Fachbereich:"), " Maschinenbau"]),
            ], className="mb-3"),

            html.Hr(),

            html.H4("📌 Kontakt und Feedback"),
            html.P("Für Rückfragen, Feedback oder Anregungen:", className="mb-2"),
            html.Ul([
                html.Li(html.B("Name: Dennis Marvin Lank")),
                html.Li(html.B("E-Mail: dennismarvinlank@gmail.de")),
                html.Li(html.A("GitHub-Repository der Applikation", href="https://github.com/DennisLank/BA_Quanser_WebApp", target="_blank")),
            ]),

            html.Div(className="text-center my-4", children=[
                html.H5("Viel Erfolg und Freude bei der Nutzung!"),
                html.Img(src="/assets/qarm_image2.png", style={"maxWidth": "50%", "height": "auto"})
            ])
        ], fluid=True)