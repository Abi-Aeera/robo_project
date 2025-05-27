# vision_sensor.py
import cv2
import mediapipe as mp

class VisionSensor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.hands = mp.solutions.hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gesture(self):
        success, frame = self.cap.read()
        if not success:
            return None

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)
        if results.multi_hand_landmarks:
            # Simplified: you can later add gesture recognition here
            return "wave"  # placeholder
        return None

    def release(self):
        self.cap.release()
