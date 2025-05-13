# Webbasierte Steuerungsplattform für den Quanser QArm mit KI-Integration

## Einleitung
Dieses Repository enthält den vollständigen Projektordner meiner Bachelorarbeit  
**„Intelligente Robotersteuerung durch eine webbasierte Mensch-Maschine-Schnittstelle mit modularer KI-Integration“**.

Die Anwendung wurde mit dem Python-Framework Dash entwickelt und dient als intuitives Steuer- und Visualisierungssystem für den Quanser QArm Roboterarm.  
Neben der manuellen Robotersteuerung integriert das System KI-gestützte Objekterkennung mit YOLOv11 sowie eine Sprachsteuerung (STT/TTS), um die Interaktion zwischen Mensch und Maschine intuitiver zu gestalten.

## Hauptfunktionen
- **Dashboard**: Übersicht und Einführung in die Nutzung der Applikation.
- **Manuelle Kontrolle**: Steuerung des Roboterarms über Gelenkwinkel, Koordinatenfahrt und LED-Farbsteuerung.
- **Live-Feed**: Echtzeitansicht des Arbeitsbereichs mit RGB- und Tiefenkameramodus.
- **Scan-Funktion**: Automatisierte Objekterkennung und -lokalisierung mittels YOLOv11, inklusive Pick & Place-Operationen.
- **YOLO-Modellverwaltung**: Upload und Verwaltung eigener YOLOv11-Modelle sowie Erstellung individueller Trainingsdatensätze.  
  ➔ Zur Unterstützung des Trainingsprozesses steht ein begleitendes Google Colab Notebook zur Verfügung.
- **Sprachsteuerung**: Regelbasierte Steuerung zentraler Funktionen per Sprachbefehl (STT/TTS).

## Systemvoraussetzungen
- Windows 10
- Funktionierende Internetverbindung (für initialen Setup und STT)
- Vorinstallierte Software:
  - **Git** (zur automatisierten Klonung des Repositories)
  - **Anaconda oder Miniconda** (zur Verwaltung der Python-Umgebung)
  - **MySQL-Server** (lokal installiert und konfiguriert)
  - **QUARC-Control-Suite** (Quanser, Installation erforderlich für Hardwareansteuerung)

## Installation & Ausführung
1. Prüfen, ob alle Systemvoraussetzungen erfüllt sind.
2. Die Datei **`start_quanser.exe`** ausführen, welche automatisch folgende Schritte durchführt:
   - Klonen des Repositories
   - Erstellen einer Python-Umgebung für die Anwendung (mit Conda)
   - Installieren aller benötigten Pakete (requirements.txt)
   - Starten der Webanwendung
3. Die Applikation läuft anschließend lokal unter:  
   [http://localhost:8050]

Das zentrale Hauptmodul ist **`dash_app.py`** – es wird durch den Startprozess automatisch ausgeführt.

## Hintergrund
Diese Anwendung wurde im Rahmen meiner Bachelorarbeit im Studiengang Maschinenbau an der Ostfalia Hochschule für angewandte Wissenschaften entwickelt.  
Ziel war es, eine modulare, KI-gestützte und benutzerfreundliche Steuerungsplattform für den Quanser QArm Roboterarm zu realisieren.

## Weitere Informationen
- Die Landingpage der Webanwendung bietet einen Überblick über sämtliche Funktionen.
- Die vollständige technische und konzeptionelle Dokumentation befindet sich in der zugehörigen Bachelorarbeit.

## Kontakt
Dennis Marvin Lank  
E-Mail: dennismarvinlank@gmail.com

## Technische Hinweise
Diese Applikation dient als Prototyp für Demonstrations- und Forschungszwecke.
Trotz umfassender Tests können vereinzelte Fehler im praktischen Betrieb nicht vollständig ausgeschlossen werden und bieten Potenzial für zukünftige Weiterentwicklungen.
