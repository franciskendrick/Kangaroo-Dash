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


class Layer:
    def init(self, filename, pos):
        path = f"{resources_path}/backgrounds"

        self.image = pygame.image.load(
            f"{path}/{filename}.png")
        self.x, self.y = pos
        self.wd, self.ht = self.image.get_size()

        self.moving = False

    def draw(self, display):
        if self.moving:
            display.blit(self.image, (self.x_offset, self.y))  # top left
            display.blit(self.image, (self.x_offset + self.wd, self.y))  # top-right
            # display.blit(self.image, [self.x_offset, self.y_offset + self.ht])  # bottom-left
            # display.blit(self.image, [self.x_offset + self.wd, self.y_offset + self.ht])  # bottom-right
        else:
            display.blit(self.image, (self.x, self.y))

    def move(self, velocity):
        self.moving = True

        self.x -= velocity

        self.x_offset = (0 - self.x % self.wd)


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