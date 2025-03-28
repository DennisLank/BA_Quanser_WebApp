import cv2, os, time
import numpy as np
import pyrealsense2 as rs
from sklearn.cluster import KMeans
from ultralytics import YOLO


class Camera:
    """
    Diese Klasse stellt die Verbindung zur Intel RealSense D415 her und ermöglicht:
    - Das Starten und Stoppen des Kamerastreams (RGB- und Tiefenbilder).
    - Die Erfassung von synchronen Bildpaaren als NumPy-Arrays.
    - Die Anwendung eines YOLO-Modells zur Objekterkennung. [ACHTUNG: ab YOLOv8-Architektur!]
    - Die Berechnung von 3D-Koordinaten aus 2D-Pixelpositionen (unter Verwendung der Tiefeninformationen).
    - Die Transformation der ermittelten Objektpositionen in ein Roboterkoordinatensystem.
    """
    def __init__(self, default_model_path="YOLO_Modelle/YOLOv11_default.pt"):
        """
        Initialisiert das Kameraobjekt und lädt ein vorab trainiertes YOLO-Modell.
        
        :param default_model_path: Standardpfad zum YOLO-Modell.
        """
        self.pipeline = None
        self.current_model_path = default_model_path
        self.model = YOLO(self.current_model_path)
    
    def connect(self):
        """
        Versucht, die RealSense-Kamera zu initialisieren und zu starten.
        Konfiguriert dabei sowohl den Tiefen- als auch den Farbstream sowie das Alignment-Modul.
        
        :return: True, wenn die Kamera erfolgreich gestartet wurde, andernfalls False.
        """
        try:
            # Prüfe, ob überhaupt ein Gerät angeschlossen ist.
            ctx = rs.context()
            devices = ctx.devices
            if len(devices) == 0:
                print("Kein RealSense Gerät angeschlossen.")
                return False
            
            # Konfiguration des Kamera-Streams
            self.pipeline = rs.pipeline()
            self.config = rs.config()
            self.config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
            self.config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
            self.pipeline_profile = self.pipeline.start(self.config)
            
            # Ausrichtung der Tiefen- und Farbbilder
            self.align = rs.align(rs.stream.color)
            
            # Ermittlung des Tiefenskalierungsfaktors
            profile = self.pipeline.get_active_profile()
            depth_sensor = profile.get_device().first_depth_sensor()
            self.depth_scale = depth_sensor.get_depth_scale()

            print(f"[INFO] RealSense-Kamera erfolgreich gestartet (1280x720, 30 FPS). Tiefenskalierung: {self.depth_scale:.6f}")
            return True
        except Exception as e:
            print(f"[FEHLER] Kamera konnte nicht gestartet werden: {e}")
            return False
    
    def get_stream(self):
        """
        Erfasst ein synchronisiertes Bildpaar (Farbbild und Tiefenbild) von der Kamera.
        
        :return: Tuple (color_image, depth_image) als NumPy-Arrays oder (None, None) bei Fehlern.
        """
        try:
            ctx = rs.context()
            devices = ctx.devices
            if len(devices) == 0:
                return None, None
            
            frames = self.pipeline.wait_for_frames(1000) # max 1s warten
            aligned_frames = self.align.process(frames)

            color_frame = aligned_frames.get_color_frame()
            depth_frame = aligned_frames.get_depth_frame()

            if not color_frame or not depth_frame:
                raise ValueError("Keine gültigen Frames von der Kamera erhalten.")

            # Konvertiere Frames in NumPy-Arrays
            color_image = np.asanyarray(color_frame.get_data())
            depth_image = np.asanyarray(depth_frame.get_data())

            return color_image, depth_image
        except Exception as e:
            return None, None

    def close_connection(self):
        """Beendet die Verbindung zur Kamera"""
        self.pipeline.stop()
        print("[INFO] Verbindung zur RealSense-Kamera wurde geschlossen.")

    def check_connection(self):
        """
        Hintergrundprozess, der die Kamera-Verbindung alle {Intervall} Sekunden überprüft.

        :return: True, wenn eine aktive Verbindung besteht, andernfalls False.
        """
        try:
            color_image, depth_image = self.get_stream()
            if color_image is None or depth_image is None:
                return False
            else:
                return True
        except:
            return False

    def load_new_model(self, new_model_path):
        """
        Lädt ein neues YOLO-Modell.
        
        :param new_model_path: Relativer Pfad zum neuen YOLO-Modell.
        """
        full_model_path = os.path.join("YOLO_Modelle", new_model_path)
        self.model = YOLO(full_model_path)
        self.current_model_path = full_model_path
        print(f"[INFO] YOLO-Modell erfolgreich gewechselt: {new_model_path}")

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
    def pixel_to_pointcloud(self, x, y, depth_value):
        """
        Wandelt einen Bildpunkt (x, y) und seinen Tiefenwert in eine 3D-Koordinate um.
        
        :return: NumPy-Array mit den kartesischen Koordinaten [X, Y, Z] in Metern.
        """
        z = depth_value * self.depth_scale  # Umwandlung in Meter
        x = (x - self.cx) * z / self.fx
        y = (y - self.cy) * z / self.fy
        return np.array([x, y, z])
    
    def detect_objects(self, qarm, confidence_threshold = 0.825):
        """
        Erkennt Objekte im Farbbild mithilfe eines YOLO-Modells und berechnet deren 3D-Koordinaten.
        
        :param qarm: Roboterarm für die Berechnung der Koordinaten
        :param confidence_threshold: Mindestkonfidenz, ab der eine Erkennung akzeptiert wird.
        :return: Liste mit Detektionsdaten + Name des Detektionsbildes + Pfad
        """
        # Alignment initialisieren
        self.align_to = rs.stream.color
        self.align = rs.align(self.align_to)

        # Intrinsische Parameter
        self.intrinsics = self.pipeline_profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()
        self.fx = self.intrinsics.fx
        self.fy = self.intrinsics.fy
        self.cx = self.intrinsics.ppx
        self.cy = self.intrinsics.ppy

        
        color_image, depth_image = self.get_stream() # Bild erhalten
        results = self.model(color_image) # YOLO-Modell anwenden
        detections = []  # Liste für die Detektionen

        for box in results[0].boxes:
            coords = box.xyxy[0].tolist()  # Extraktion der Bounding-Box-Koordinaten
            conf = float(box.conf[0])
            if conf < confidence_threshold:
                continue

            x1, y1, x2, y2 = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])
            class_idx = int(box.cls[0])
            class_name = results[0].names[class_idx]

            # Boundary-Box mit Label einzeichnen (optional)
            cv2.rectangle(color_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{class_name}: {conf:.2f}"
            cv2.putText(color_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 2)

            # Tiefenwerte innerhalb der Bounding Box extrahieren
            depth_crop = depth_image[y1:y2, x1:x2].copy()
            rows, cols = depth_crop.shape
            if rows == 0 or cols == 0:
                continue

            # Meshgrid für Pixel-Koord
            c, r = np.meshgrid(np.arange(cols), np.arange(rows))
            depth_values = depth_crop.flatten()
            x_flat = c.flatten() + x1
            y_flat = r.flatten() + y1

            # Tiefenwert sollte > 0 sein
            valid = depth_values > 0
            if np.count_nonzero(valid) == 0:
                print(f"[WARNUNG] Keine gültigen Tiefenwerte für '{class_name}' erkannt.")
                continue

            x_valid = x_flat[valid]
            y_valid = y_flat[valid]
            depth_valid = depth_values[valid]

            # 3D-Koordinaten berechnen
            points = []
            for xi, yi, di in zip(x_valid, y_valid, depth_valid):
                point = self.pixel_to_pointcloud(xi, yi, di)
                points.append(point)
            points = np.array(points)

            # KMeans-Clustering zur Trennung von Objekt und Hintergrund (mit k=2)
            kmeans = KMeans(n_clusters=2, random_state=0).fit(points[:, 2].reshape(-1, 1))
            labels = kmeans.labels_

            # Näheres Cluster betrachten
            object_cluster = points[labels == (kmeans.cluster_centers_.argmin())]

            # Berechnung des Objektschwerpunkts
            centroid = np.mean(object_cluster, axis=0)

            # Berechnung des Objektschwerpunkts
            centroid[2] += 0.03
            grasp_point_in_base = qarm.cam_to_rob(centroid)
            
            # ------------------------
            # z-Koord fehlerhaft? --> HIER: z manuell erhöhen (Makro-Scan-Position)
            # Anpassung der Z-Koordinate basierend auf der Entfernung zur Basis --> vorne tiefer, hinten höher
            sum_xy = abs(grasp_point_in_base[0]) + abs(grasp_point_in_base[1])
            z_offset = 0.03 + (sum_xy - 0.15) / (1.6 - 0.15) * (0.13 - 0.03)
            grasp_point_in_base[2] = z_offset

            # Speicherung der Detektionsdaten
            detection = {
                'class_name': class_name,
                'bbox': [x1, y1, x2, y2],
                'confidence': conf,
                'grasp_point': grasp_point_in_base
            }
            detections.append(detection)
            print(f"[INFO] Detektion: {detection}")

        # Speicherung des annotierten Bildes mit Bounding Boxes
        output_dir = "Scans/makro"
        timestamp = time.time()
        img_filename = f"detection_{timestamp:.0f}.png"
        output_path = os.path.join(output_dir, img_filename)
        cv2.imwrite(output_path, color_image)
        print(f"[INFO] Detektionsergebniss gespeichert in: {output_path}")

        if not detections:
            print("[INFO] Keine Objekte erkannt.")
            return None

        return detections, img_filename, output_path



    def get_depth_frame_raw(self):
        """
        Liefert den originalen Tiefenframe (rs.frame), ohne ihn in ein NumPy-Array umzuwandeln.
        Wird für den MJPEG-Stream verwendet, damit der Colorizer damit arbeiten kann.
        
        :return: Tiefenframe-Objekt (rs.frame) oder None bei Fehlern.
        """
        try:
            frames = self.pipeline.wait_for_frames(1000)
            aligned_frames = self.align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            if not depth_frame:
                raise ValueError("[WARNUNG] Kein gültiger Tiefenframe empfangen.")
            return depth_frame
        except Exception as e:
            print(f"[FEHLER] Fehler beim Abrufen des rohen Tiefenframes: {e}")
            return None