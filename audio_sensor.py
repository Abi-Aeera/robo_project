# audio_sensor.py
import speech_recognition as sr

class AudioSensor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=3)
        try:
            command = self.recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return None
