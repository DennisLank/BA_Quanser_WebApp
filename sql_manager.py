import mysql.connector
from mysql.connector import Error

class MySQLManager:
    """
    Verwaltung der MySQL-Datenbankverbindung und Datenoperationen für Objekterkennungsdaten.
    Diese Klasse ermöglicht das Verbinden, Erstellen, Einfügen und Bereinigen von Datenbanken und Tabellen.
    """

    def __init__(self, host="localhost", user="root", password="123SA2", database="objects_db"):
        """
        Initialisiert den MySQLManager mit Verbindungsdetails.

        Args:
            host (str): Hostadresse der Datenbank. Standard ist "localhost".
            user (str): Benutzername für die MySQL-Datenbank.
            password (str): Passwort für die MySQL-Datenbank.
            database (str): Name der Datenbank (Standard: "objects_db").
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Verbindet sich mit der MySQL-Datenbank und erstellt bei Bedarf die Objekttabelle.

        Raises:
            ConnectionError: Falls die Verbindung zur Datenbank fehlschlägt.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database};")
            cursor.execute(f"USE {self.database};")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS objects (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Image VARCHAR(255),
                    X FLOAT, Y FLOAT, Z FLOAT,
                    Y1 FLOAT, Y2 FLOAT, Y3 FLOAT, Y4 FLOAT, Y5 FLOAT,
                    Objektart VARCHAR(255),
                    Confidence FLOAT,
                    Bild_Pfad VARCHAR(255)
                );
            """)
            self.clear_table("objects")  # Falls die Tabelle nicht geleert werden soll -> auskommentieren
            print("[INFO] MySQL-Datenbank und Tabelle erfolgreich eingerichtet.")
        except Error as e:
            if e.errno == 1045:  # MySQL-Fehlercode für falsches Passwort/Nutzername
                print(f"[Fehler] Zugriff verweigert (falsche Login-Daten). Überprüfe Benutzername/Passwort.")
            else:
                print(f"[FEHLER] Verbindung zur MySQL-Datenbank fehlgeschlagen: {e}")
            self.connection = None  # Verbindung als ungültig markieren
        
    def check_connection(self):
        """
        Überprüft, ob eine aktive Verbindung zur MySQL-Datenbank besteht.

        Returns:
            bool: True, wenn die Verbindung aktiv ist, sonst False.
        """
        if self.connection is None:
            return False
        try:
            self.connection.ping(reconnect=False, attempts=1, delay=1)
            return True
        except:
            self.connection = None
            return False

    def clear_table(self, table_name="objects"):
        """
        Löscht alle Daten in der angegebenen Tabelle.

        Args:
            table_name (str): Name der Tabelle, die bereinigt werden soll (Standard: "objects").

        Raises:
            ConnectionError: Falls keine aktive Verbindung zur Datenbank besteht.
            Error: Falls das Löschen der Daten fehlschlägt.
        """
        if not self.connection:
            raise ConnectionError("[FEHLER] Keine aktive Verbindung zur Datenbank.")
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"TRUNCATE TABLE {table_name};")
            self.connection.commit()
            print(f"[INFO] Alle Einträge aus der Tabelle '{table_name}' wurden gelöscht.")
        except Error as e:
            print(f"[FEHLER] Konnte die Tabelle '{table_name}' nicht bereinigen: {e}")

    def insert_object_data(self, object_data):
        """
        Fügt einen neuen Datensatz in die Tabelle ein.

        Args:
            object_data (dict): Ein Dictionary mit den einzufügenden Daten.

        Raises:
            ConnectionError: Falls keine aktive Verbindung zur Datenbank besteht.
            Error: Falls das Einfügen der Daten fehlschlägt.
        """
        if not self.connection:
            raise ConnectionError("Keine aktive Verbindung zur MySQL-Datenbank.")
        try:
            cursor = self.connection.cursor()
            insert_query = """
                INSERT INTO objects (Image, X, Y, Z, Y1, Y2, Y3, Y4, Y5, Objektart, Confidence, Bild_Pfad)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                object_data["Image"],
                object_data["X"], object_data["Y"], object_data["Z"],
                object_data["Y1"], object_data["Y2"], object_data["Y3"], object_data["Y4"], object_data["Y5"],
                object_data["Objektart"], object_data["Confidence"],
                object_data["Bild_Pfad"]
            ))
            self.connection.commit()
            print(f"[INFO] Datensatz für '{object_data['Image']}' erfolgreich gespeichert.")
        except Error as e:
            print(f"[FEHLER] Einfügen der Daten in die Tabelle fehlgeschlagen: {e}")
            raise e

    def close_connection(self):
        """
        Schließt die Verbindung zur MySQL-Datenbank.
        """
        if self.connection:
            self.connection.close()
            self.connection = None
            print("[INFO] Verbindung zur MySQL-Datenbank erfolgreich geschlossen.")
        else:
            print("[WARNUNG] Keine aktive Verbindung zum Schließen vorhanden.")

    def remove_duplicates_and_reset_ids(self, duplicate_ids):
        """
        Entfernt doppelte Einträge aus der Tabelle und setzt die ID-Zählung zurück.

        Args:
            duplicate_ids (list): Liste mit den IDs der zu löschenden Duplikate.

        Raises:
            Error: Falls das Entfernen der Duplikate fehlschlägt.
        """
        try:
            cursor = self.connection.cursor()
            # Löscht alle Einträge mit den übergebenen IDs
            ids_str = ", ".join(map(str, duplicate_ids))
            cursor.execute(f"DELETE FROM objects WHERE id IN ({ids_str});")
            self.connection.commit()

            # IDs neu sortieren
            cursor.execute("SET @count = 0;")
            cursor.execute("UPDATE objects SET id = (@count:=@count+1) ORDER BY id;")
            cursor.execute("ALTER TABLE objects AUTO_INCREMENT = 1;")
            self.connection.commit()
            print("[INFO] Doppelte Einträge entfernt und IDs zurückgesetzt.")
        except Error as e:
            print(f"[FEHLER] Konnte die Duplikate nicht entfernen oder IDs nicht zurücksetzen: {e}")
            raise e
        