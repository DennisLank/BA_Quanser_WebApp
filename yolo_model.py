import os
from ultralytics import YOLO
from dash import Input, Output, State

class YOLOModelController:
    """
    Diese Klasse verwaltet die YOLO-Modellverwaltung innerhalb der Dash-Applikation.

    Funktionen:
    - Laden eines YOLO-Modells basierend auf der Benutzerwahl im Dropdown-Menü.
    - Speicherung und Verwaltung des aktuell geladenen Modells.
    - Automatische Aktualisierung der Dropdown-Optionen basierend auf verfügbaren Modellen.

    Attribute:
        current_model_path: Pfad des aktuell geladenen YOLO-Modells.
        model: Instanz des geladenen YOLO-Modells.
    """

    def __init__(self, app, default_model_path="YOLO_Modelle/YOLOv11_default.pt"):
        """
        Initialisiert den YOLOModelController und lädt das Standardmodell.

        Args:
            app: Die Dash-App-Instanz zur Registrierung der Callbacks.
            default_model_path: Pfad zum Standardmodell (Default: YOLOv11_default.pt).
        """
        self.current_model_path = default_model_path
        self.model = YOLO(self.current_model_path)
        self.register_callbacks(app)

    def get_current_model_name(self):
        """
        Gibt den Namen des aktuell geladenen Modells zurück.

        Returns:
            str: Name der aktuell verwendeten YOLO-Modell-Datei.
        """
        return os.path.basename(self.current_model_path)
    
    def load_model(self, new_model_path):
        """
        Lädt ein neues YOLO-Modell aus dem angegebenen Pfad.

        Args:
            new_model_path (str): Pfad zur neuen YOLO-Modell-Datei.

        Returns:
            str: Name des neu geladenen Modells.
        """
        if new_model_path != self.current_model_path:
            self.model = YOLO(new_model_path)
            self.current_model_path = new_model_path
            return self.get_current_model_name()

    def get_model(self):
        """
        Gibt das aktuell geladene YOLO-Modell zurück.

        Returns:
            YOLO: Instanz des aktuell geladenen Modells.
        """
        return self.model
        
    def register_callbacks(self, app):
        """
        Registriert den Callback zur Aktualisierung der YOLO-Dropdown-Optionen.

        Args:
            app: Die Dash-App-Instanz, in der der Callback registriert wird.
        """
        @app.callback(
            [Output("yolo-dropdown", "options"),
             Output("yolo-dropdown", "value")],
            Input("update-setting-icons", "n_intervals"),
            State("yolo-dropdown", "value")
        )
        def update_yolo_dropdown(n_intervals, current_value):
            """
            Aktualisiert die Dropdown-Optionen für verfügbare YOLO-Modelle.

            Args:
                n_intervals (int): Zeitintervall-Trigger.
                current_value (str): Aktuell im Dropdown gewähltes Modell.

            Returns:
                tuple: (Liste der Modelloptionen, aktuell gewähltes Modell).
            """
            path = os.path.join(os.getcwd(), "YOLO_Modelle")
            options = [{"label": f, "value": f} for f in sorted(os.listdir(path))] if os.path.exists(path) else [{"label": "Kein YOLO Modell gefunden", "value": None}]

            current_loaded = self.get_current_model_name()

            if current_value is not None and current_value != current_loaded:
                self.load_model(f"YOLO_Modelle/{current_value}")
                return options, current_value

            return options, current_loaded
