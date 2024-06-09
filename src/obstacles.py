from functions import clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class BigCactus:
    def __init__(self, size, add_x):
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/big_cactus.png")
        images = clip_set_to_list_on_xaxis(spriteset)
        self.image = images[size]
        self.size = self.image.get_size()

        self.x = (add_x * 16) + 256
        self.y = 79
        self.vel = 2

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.vel


class SmallCactus:
    def __init__(self, size, add_x):
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/small_cactus.png")
        images = clip_set_to_list_on_xaxis(spriteset)
        self.image = images[size]
        self.size = self.image.get_size()

        self.x = (add_x * 16) + 256
        self.y = 95
        self.vel = 2

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.vel


class Bird:
    def __init__(self, height, add_x):
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/bird.png")
        self.images = clip_set_to_list_on_xaxis(spriteset)
        self.idx = 0

        self.size = self.images[0].get_size()

        self.x = (add_x * 16) + 256
        self.y = (16 * (4 + height)) + 2
        self.vel = 2

    def draw(self, display):
        # Update frame
        if self.idx >= len(self.images) * 10:
            self.idx = 0

        # Draw
        img = self.images[self.idx // 10]
        display.blit(img, (self.x, self.y))

        # Update frame
        self.idx += 1

    def update(self):
        self.x -= self.vel