import re
import threading
import pyttsx3
import speech_recognition as sr


def speak(text):
    """
    Gibt den übergebenen Text per Text-to-Speech (TTS) aus.

    Args:
        text (str): Der auszugebende Text.
    """
    def _speak():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=_speak).start()

def listen_command():
    """
    Nimmt einen Sprachbefehl über das Mikrofon auf und gibt den erkannten Text zurück.

    Returns:
        str: Der erkannte Sprachbefehl oder ein leerer String bei Fehlern.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[INFO] Aufnahme startet...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="de-DE")
        print(f"[INFO] Erkannt: {command}")
        return command
    except sr.UnknownValueError:
        speak("Spracherkennung konnte den Befehl nicht verstehen.")
        return ""
    except sr.RequestError as e:
        speak("Fehler bei der Spracherkennung.")
        return ""

def process_stt_command(command, qarm):
    """
    Parst den STT-Befehl und löst entsprechende Aktionen aus.
    Unterstützte Befehle:
      • "Start/Home-Position anfahren."
      • "Setze RGB auf rot/grün/blau"
      • "Zeige mir das Farbbild" / "Zeige mir das Tiefenbild"
      • "Bewege die Basis nach links/rechts"
      • "Bewege die Schulter hoch/runter"
      • "Bewege den Ellbogen hoch/runter"
      • "Scan durchführen"
      • "Platziere Objekt {id} zu Objekt {id}"
      • "Platziere Objekt {id} zu Koordinaten x gleich {x} und y gleich {y}"
      
    Args:
        command (str): Der erkannte Sprachbefehl.
        qarm (QArmControl): Instanz der Robotersteuerung.

    Returns:
        dict: Ein Dictionary mit Steuerungsinformationen:
            - feedback (str): Rückmeldung für TTS und Toast.
            - tab (str): Name des Tabs, zu dem gewechselt werden soll.
            - simulate_click (str): ID des zu simulierenden Buttons.
            - set_dropdown1 (str, optional): Wert für das erste Dropdown (Variante 1 Pick & Place).
            - set_dropdown2 (str, optional): Wert für das zweite Dropdown (Variante 1 Pick & Place).
            - set_dropdown_single (str, optional): Wert für das einzelne Dropdown (Variante 2 Pick & Place).
            - x_coord (float, optional): X-Koordinate für das Platzieren.
            - y_coord (float, optional): Y-Koordinate für das Platzieren.
    """
    cmd_lower = command.lower().strip()
    result = {"feedback": "", 
              "tab": None, 
              "simulate_click": None, 
              "set_dropdown1": None, 
              "set_dropdown2": None, 
              "set_dropdown_single": None,
              "x_coord": None,
              "y_coord": None
              }

    # Home-Position anfahren
    if "startposition" in cmd_lower or "start position" in cmd_lower or "home" in cmd_lower:
        result["feedback"] = "Die Start-Position wurde angefahren."
        qarm.go_to("home")

    # LED-Steuerung
    elif "rgb" in cmd_lower and "rot" in cmd_lower:
        result["feedback"] = "Ich setze die RGB nun auf rot."
        result["tab"] = "manual_control"
        result["simulate_click"] = "btn-led-rot"
    elif "rgb" in cmd_lower and ("grün" in cmd_lower or "gruen" in cmd_lower):
        result["feedback"] = "Ich setze die RGB nun auf grün."
        result["tab"] = "manual_control"
        result["simulate_click"] = "btn-led-gruen"
    elif "rgb" in cmd_lower and "blau" in cmd_lower:
        result["feedback"] = "Ich setze die RGB nun auf blau."
        result["tab"] = "manual_control"
        result["simulate_click"] = "btn-led-blau"
    
    # Live-Feed: Farbbild / Tiefenbild
    elif "farbbild" in cmd_lower or "farb" in cmd_lower:
        result["feedback"] = "Ich öffne das Farbbild."
        result["tab"] = "live_feed"
        result["simulate_click"] = "btn-extra-farbbild"
    elif "tiefenbild" in cmd_lower or "tiefen" in cmd_lower:
        result["feedback"] = "Ich öffne das Tiefenbild."
        result["tab"] = "live_feed"
        result["simulate_click"] = "btn-extra-tiefenbild"
    

    # Roboterbewegung
    # Basis
    elif "basis" in cmd_lower:
        result["tab"] = "manual_control"
        if "links" in cmd_lower:
            result["feedback"] = "Ich bewege die Basis nach links."
            result["simulate_click"] = "btn-base-plus"
        elif "rechts" in cmd_lower:
            result["feedback"] = "Ich bewege die Basis nach rechts."
            result["simulate_click"] = "btn-base-minus"
    # Schulter
    elif "schulter" in cmd_lower:
        result["tab"] = "manual_control"
        if "hoch" in cmd_lower or "oben" in cmd_lower:
            result["feedback"] = "Ich bewege die Schulter hoch."
            result["simulate_click"] = "btn-shoulder-minus"
        elif "runter" in cmd_lower or "unten" in cmd_lower:
            result["feedback"] = "Ich bewege die Schulter runter."
            result["simulate_click"] = "btn-shoulder-plus"
    # Ellbogen
    elif "ellbogen" in cmd_lower:
        result["tab"] = "manual_control"
        if "hoch" in cmd_lower or "oben" in cmd_lower:
            result["feedback"] = "Ich bewege den Ellbogen hoch."
            result["simulate_click"] = "btn-elbow-minus"
        elif "runter" in cmd_lower or "unten" in cmd_lower:
            result["feedback"] = "Ich bewege den Ellbogen runter."
            result["simulate_click"] = "btn-elbow-plus"
    
    
    # Scan starten
    elif "scan" in cmd_lower:
        result["feedback"] = "Ich starte den Scan."
        result["tab"] = "scan"
        result["simulate_click"] = "btn-scan"
    
    
    # Pick & Place
    elif "platziere objekt" in cmd_lower:
        result["tab"] = "scan"
        match1 = re.search(r"platziere objekt\s+(\d+)\s+zu objekt\s+(\d+)", cmd_lower)
        # Neue Variante 2: explizit: "platziere objekt {id} zu koordinaten x gleich {x} und y gleich {y}"
        match2 = re.search(r"platziere objekt\s+(\d+)\s+zu koordinaten\s+x\s*=\s*([-]?[\d\.,]+)\s+und\s+y\s*=\s*([-]?[\d\.,]+)", cmd_lower)
        
        # Objekt zu Objekt
        if match1:
            obj_from = match1.group(1)
            obj_to = match1.group(2)
            result["feedback"] = f"Ich platziere Objekt {obj_from} zu Objekt {obj_to}."
            result["set_dropdown1"] = obj_from
            result["set_dropdown2"] = obj_to
            result["simulate_click"] = "btn-place-objects-compare"
        
        # Objekt zu Koord
        elif match2:
            obj_id = match2.group(1)
            x_str = match2.group(2).replace(",", ".")
            y_str = match2.group(3).replace(",", ".")
            try:
                x_coord = float(x_str)
                y_coord = float(y_str)
            except Exception as e:
                x_coord = None
                y_coord = None
            result["feedback"] = f"Ich platziere Objekt {obj_id} zu Koordinaten x = {x_coord} und y = {y_coord}."
            result["simulate_click"] = "btn-place-object-coord"
            result["set_dropdown_single"] = obj_id
            result["x_coord"] = x_coord
            result["y_coord"] = y_coord
            
        else:
            result["feedback"] = f"{command} - Pick & Place Befehl nicht korrekt erkannt."

    else:
        result["feedback"] = f"Unbekannter Befehl: {command}."


    speak(result["feedback"])
    return result
