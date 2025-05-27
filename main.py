# main.py
from vision_sensor import VisionSensor
from audio_sensor import AudioSensor
from display import Display
from speaker import Speaker
from robot_brain import RobotBrain
import pygame

vision = VisionSensor()
audio = AudioSensor()
display = Display()
speaker = Speaker()
brain = RobotBrain(vision, audio, display, speaker)

try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gesture = vision.detect_gesture()
        if gesture:
            brain.respond_to_gesture(gesture)

        command = audio.listen()
        if command:
            brain.respond_to_command(command)

finally:
    vision.release()
    display.close()
