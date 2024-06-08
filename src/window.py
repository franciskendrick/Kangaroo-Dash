import pygame
import time
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Window:
    def __init__(self):
        # Window
        self.rect = pygame.Rect(0, 0, 256, 128)
        self.enlarge = 4

        # Framerate
        self.framerate = 60

    def update_gameinfo(self):
        pass


class Background:
    def __init__(self):
        path = f"{resources_path}/backgrounds"

        self.background = (
            pygame.image.load(f"{path}/background.png"), (0, 0))
        self.middleground = (
            pygame.image.load(f"{path}/middleground.png"), (0, 35))
        self.foreground = (
            pygame.image.load(f"{path}/foreground.png"), (0, 43))
        self.floor = (
            pygame.image.load(f"{path}/floor.png"), (0, 107))

    def draw(self, display):
        display.blit(*self.background)
        display.blit(*self.middleground)
        display.blit(*self.foreground)
        display.blit(*self.floor)


window = Window()