import time
import numpy as np
from quanser.p_QArm import QArm, QArmUtilities

class QArmControl:
    """
    Diese Klasse verwaltet die Steuerung des Quanser QArm-Roboters.
    Sie ermöglicht Bewegungen, Statusabfragen, Greifsteuerung und Koordinatentransformationen.
    """

    def __init__(self):
        self.my_arm = None

    def connect(self):
        """
        Stellt die Verbindung zum Quanser QArm her und initialisiert notwendige Parameter.

        Returns:
            bool: True, wenn die Verbindung erfolgreich hergestellt wurde, andernfalls False.
        """
        try:
            self.my_arm = QArm(hardware=1)
            self.myArmUtilities = QArmUtilities()

            self.joint_limits_degrees = {
                "base": (-170, 170),
                "shoulder": (-85, 85),
                "elbow": (-95, 75),
                "wrist": (-160, 160)
            }
            self.joint_limits_radians = {key: (np.radians(lim[0]), np.radians(lim[1])) for key, lim in self.joint_limits_degrees.items()}

            # Geschätzte Hand-Augen-Kalibrierung (Transformation zwischen Kamera und Greifer)
            self.R_cam2gripper = [[0,-1,0],[1,0,0],[0,0,1]]
            self.t_cam2gripper = np.array([[0.058],[-0.038],[-0.2]])
            print(f"[INFO] Kalibrierdaten geladen: R = {self.R_cam2gripper}, t = {self.t_cam2gripper}")

            self.my_arm.read_std() # aktuelle Robo-Pos
            joint_pos = self.my_arm.measJointPosition
            _, _, _, _, p_gripper_in_base, R_gripper_in_base = self.myArmUtilities.qarm_forward_kinematics(joint_pos[:4])
            global robot_position, robot_rotation
            robot_position = p_gripper_in_base
            robot_rotation = R_gripper_in_base
            
            if self.my_arm is None:
                return False
            if not self.my_arm.card.is_valid():
                return False
            else:
                print("[INFO] Roboter erfolgreich verbunden.")
                return True
        except Exception as e:
            print(f"[FEHLER] Verbindungsfehler: {e}")
            return False

    def check_connection(self):
        """
        Überprüft, ob der Roboter aktuell verbunden ist.

        Returns:
            bool: True, wenn eine aktive Verbindung besteht, andernfalls False.
        """
        if self.my_arm is None:
            return False
        if not self.my_arm.card.is_valid():
            return False
        else:
            return True
        
    def check_base_limits(self, position, threshold=0.005):
        """
        Überprüft, ob die Zielposition innerhalb der Basisgrenzen liegt.

        Args:
            position (list): Die XYZ-Koordinaten der Zielposition.
            threshold (float, optional): Zusätzlicher Sicherheitsabstand. Standardwert: 0.005.

        Raises:
            BaseLimitError: Wenn die Position zu nah an der Basis liegt.

        Returns:
            bool: True, wenn die Position gültig ist.
        """
        x_min, x_max = -0.11, 0.11
        y_min, y_max = -0.11, 0.11
        z_min, z_max = 0, 0.9  # z sollte nicht negativ sein, daher 0 als Untergrenze
        x, y, z = position[:3]

        # Prüfe, ob die Position innerhalb der Box liegt
        if (x_min - threshold <= x <= x_max + threshold and
            y_min - threshold <= y <= y_max + threshold and
            z_min - threshold <= z <= z_max + threshold):
            raise BaseLimitError(f"[WARNUNG] Position zu nah an der Basis: x={x:.2f}, y={y:.2f}, z={z:.2f}. Vorgang wird abgebrochen.")
        return True
    
    def check_box_limits(self, position):
        if position[2] < 0:
            raise BoxLimitError(f"Position too close to the ground. z: {position[2]}m. Aborting operation.")
        return True

    def check_joint_limits(self, joint_angles):
        base_angle, shoulder_angle, elbow_angle, wrist_angle = joint_angles
        if not self.joint_limits_radians["base"][0] <= base_angle <= self.joint_limits_radians["base"][1]:
            raise JointLimitError(f"Base angle {np.degrees(base_angle):.2f}° exceeds the limit. Aborting operation.")
        if not self.joint_limits_radians["shoulder"][0] <= shoulder_angle <= self.joint_limits_radians["shoulder"][1]:
            raise JointLimitError(f"Shoulder angle {np.degrees(shoulder_angle):.2f}° exceeds the limit. Aborting operation.")
        if not self.joint_limits_radians["elbow"][0] <= elbow_angle <= self.joint_limits_radians["elbow"][1]:
            raise JointLimitError(f"Elbow angle {np.degrees(elbow_angle):.2f}° exceeds the limit. Aborting operation.")
        if not self.joint_limits_radians["wrist"][0] <= wrist_angle <= self.joint_limits_radians["wrist"][1]:
            raise JointLimitError(f"Wrist angle {np.degrees(wrist_angle):.2f}° exceeds the limit. Aborting operation.")
        return True

    def go_to(self, coord, rotation = 0):
        """
        Bewegt den Roboterarm zu einer bestimmten Koordinate oder in die Home-Position.

        Args:
            coord (list oder str): Zielkoordinaten [x, y, z] oder "home" für die Startposition.
            rotation (float, optional): Rotation des Greifers in Grad. Standardwert: 0.
        """
        self.my_arm.read_std()
        phi = self.my_arm.measJointPosition
        if isinstance(coord, str) and coord == "home":
            print(f"Go to Home Position")
            self.my_arm.read_write_std(phiCMD=[0,0,0,0], grpCMD=phi[4])
            self.wait_until_arrived([4.500000e-01, 3.061617e-18, 4.900000e-01])
        else:
            if self.check_base_limits(coord) and self.check_box_limits(coord):
                _, phi_cmd = self.myArmUtilities.qarm_inverse_kinematics(coord, 0, phi[:4])
                phi_cmd[3] = np.radians(rotation)
                if self.check_joint_limits(phi_cmd):
                    print(f"Go to Coordinates: {coord}, set Motor-Positions: {np.degrees(phi_cmd)}")
                    self.my_arm.read_write_std(phiCMD=phi_cmd, grpCMD=phi[4])
                    self.wait_until_arrived(coord)

    def go_to_joint(self, phi):
        self.my_arm.read_std()
        phi_old = self.my_arm.measJointPosition
        _,_,_,_,coord, _ = self.myArmUtilities.qarm_forward_kinematics(phi[:4])
        if self.check_base_limits(coord) and self.check_box_limits(coord) and self.check_joint_limits(phi):
            print(f"Go to Coordinates: {coord}, set Motor-Positions: {np.degrees(phi)}")
            self.my_arm.read_write_std(phiCMD=phi, grpCMD=phi_old[4])
            self.wait_until_arrived(coord)
            
    def gripper(self, cmd):
        self.my_arm.read_std()
        phi = self.my_arm.measJointPosition
        self.my_arm.read_write_std(phiCMD = phi[:4], grpCMD=cmd)
        time.sleep(1)
        if(cmd):
            print(f"Gripper closed. POS {phi[4]}")
        else:
            print(f"Gripper opened. POS: {phi[4]}")

    def wait_until_arrived(self, dest, timeout_duration = 10, threshold= 0.05):
        global robot_position, robot_rotation
        time.sleep(1)
        start_time = time.time()
        while True:
            self.my_arm.read_std()
            joint_pos = self.my_arm.measJointPosition
            _,_,_,_,pos, _ = self.myArmUtilities.qarm_forward_kinematics(joint_pos[:4])
            distance = np.linalg.norm(pos - dest, ord=2)
            if distance <= threshold:
                start_time = time.time()
                while True:
                    self.my_arm.read_std()
                    speeds = self.my_arm.measJointSpeed
                    if(all(speed == 0 for speed in speeds)):
                        break
                    if time.time() - start_time > timeout_duration:
                        raise TimeOutError(f"Timeout: Not stationary within {timeout_duration} seconds. Aborting operation.")
                self.my_arm.read_std()
                joint_pos = self.my_arm.measJointPosition
                _,_,_,_,p_gripper_in_base, R_gripper_in_base = self.myArmUtilities.qarm_forward_kinematics(joint_pos[:4])
                robot_position = p_gripper_in_base
                robot_rotation = R_gripper_in_base
                print(f"Arrived at {p_gripper_in_base}. Target was {dest}.")
                break
            if time.time() - start_time > timeout_duration:
                raise TimeOutError(f"Timeout: Did not reach destination {dest} within {timeout_duration} seconds. Position: {p_gripper_in_base} Aborting operation.")
            time.sleep(0.1)

    def LED_Control(self, baseLED):
        # baseLED as a 3x1 numpy array 
        self.my_arm.write_LEDs(baseLED)
        print(f"LED auf {baseLED} gesetzt.")

    def basis_drehen(self, basis_winkel):
        scan_pos_joints = np.copy(self.my_arm.measJointPosition[:4])  # Gelenkposition speichern
        scan_pos_joints[0] = np.deg2rad(basis_winkel)
        self.go_to_joint(scan_pos_joints)
        return print(f"Basis wird auf {basis_winkel} gedreht.")

    def cam_to_rob(self, point_in_camera):
        """
        Transforms a point from the camera's coordinate system to the robot base frame using the
        hand-eye calibration result (homogeneous transformation matrix).
        
        :param point_in_camera: 3D point in the camera's coordinate system [x, y, z]
        :return: Transformed 3D point in the robot base frame [x, y, z]
        """
        # Step 1: Ensure the point is in homogeneous coordinates (4x1 vector)
        point_in_camera = np.append(point_in_camera, 1).reshape(4, 1)  # Add the homogeneous coordinate (1)

        # Step 2: Construct the homogeneous transformation matrix for the camera to gripper transformation
        H_cam2gripper = np.eye(4)  # Initialize as 4x4 identity matrix
        H_cam2gripper[:3, :3] = self.R_cam2gripper  # Set rotation part
        H_cam2gripper[:3, 3] = self.t_cam2gripper.flatten()  # Set translation part

        # Step 3: Transform the point from the camera frame to the gripper frame
        point_in_gripper = H_cam2gripper @ point_in_camera

        # Step 4: Get the current gripper pose in the base frame using forward kinematics
        self.my_arm.read_std()  # Read the joint positions
        joint_pos = self.my_arm.measJointPosition  # Get joint positions
        _,_,_,_,p_gripper_in_base, R_gripper_in_base = self.myArmUtilities.qarm_forward_kinematics(joint_pos)

        # Step 5: Construct the homogeneous transformation matrix for the gripper to base transformation
        H_gripper2base = np.eye(4)  # Initialize as 4x4 identity matrix
        H_gripper2base[:3, :3] = R_gripper_in_base  # Set rotation part
        H_gripper2base[:3, 3] = p_gripper_in_base.flatten()  # Set translation part

        # Step 6: Transform the point from the gripper frame to the base frame
        point_in_base = H_gripper2base @ point_in_gripper

        # Step 7: Return the transformed point (convert homogeneous back to 3D)
        return point_in_base[:3].flatten()

    def close_connection(self):
        print("[INFO] Roboter wird heruntergefahren.")
        self.my_arm.terminate()


class JointLimitError(Exception):
    pass
class BaseLimitError(Exception):
    pass
class TimeOutError(Exception):
    pass
class BoxLimitError(Exception):
    pass
class InvalidDepthError(Exception):
    pass
