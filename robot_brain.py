# robot_brain.py
class RobotBrain:
    def __init__(self, vision, audio, display, speaker=None):
        self.vision = vision
        self.audio = audio
        self.display = display
        self.speaker = speaker

    def respond_to_gesture(self, gesture):
        if gesture == "wave":
            self.display.show_text("Hello!")
            if self.speaker:
                self.speaker.speak("Hello!")

    def respond_to_command(self, command):
        if command.startswith("display"):
            msg = command.replace("display", "").strip()
            self.display.show_text(msg)
        elif command == "clear display":
            self.display.clear_display()
        elif command == "hello":
            self.display.show_text("Hi there!")
            if self.speaker:
                self.speaker.speak("Hi there!")
