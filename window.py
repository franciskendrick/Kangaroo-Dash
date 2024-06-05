import pygame

pygame.init()


class Window:
    def __init__(self):
        # Window
        self.rect = pygame.Rect(0, 0, 256, 128)
        self.enlarge = 4

        # Framerate
        self.framerate = 60

    def update_gameinfo(self):
        pass

    def update_deltatime(self):
        pass


window = Window()