# display.py
import pygame

class Display:
    def __init__(self, width=320, height=240):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Robot Display")
        self.font = pygame.font.SysFont("Courier", 20)
        self.clear_display()

    def clear_display(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def show_text(self, text):
        self.clear_display()
        rendered = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(rendered, (20, 100))
        pygame.display.flip()

    def close(self):
        pygame.quit()
