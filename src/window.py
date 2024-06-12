import pygame
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


# class Background:
#     def __init__(self):
#         path = f"{resources_path}/backgrounds"

#         self.background = (
#             pygame.image.load(f"{path}/background.png"), (0, 0))
#         self.middleground = (
#             pygame.image.load(f"{path}/middleground.png"), (0, 35))
#         self.foreground = (
#             pygame.image.load(f"{path}/foreground.png"), (0, 43))
#         self.floor = (
#             pygame.image.load(f"{path}/floor.png"), (0, 107))

#     def draw_bg(self, display):
#         display.blit(*self.background)
#         display.blit(*self.middleground)
#         display.blit(*self.foreground)

#     def draw_floor(self, display):
#         display.blit(*self.floor)


class Layer:
    def init(self, filename, pos):
        path = f"{resources_path}/backgrounds"

        self.image = pygame.image.load(
            f"{path}/{filename}.png")
        self.pos = pos

    def draw(self, display):
        display.blit(self.image, self.pos)


class Background(Layer):
    def __init__(self):
        super().__init__()

        self.init("background", (0, 0))


class Middleground(Layer):
    def __init__(self):
        super().__init__()

        self.init("middleground", (0, 35))


class Foreground(Layer):
    def __init__(self):
        super().__init__()

        self.init("foreground", (0, 43))


class Floor(Layer):
    def __init__(self):
        super().__init__()

        self.init("floor", (0, 107))


window = Window()