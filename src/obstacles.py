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
    hitbox_offsets = [
        (1, 2), 
        (2, 2), 
        (2, 2)
    ]
    hitbox_dimensions = [
        (14, 31),
        (30, 31),
        (46, 31)
    ]

    def __init__(self, size, add_x):
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/big_cactus.png")
        images = clip_set_to_list_on_xaxis(spriteset)
        self.image = images[size]
        self.dimensions = self.image.get_size()
        self.size = size

        self.x = (add_x * 16) + 256
        self.y = 79
        self.vel = 1

        offset_x, offset_y = self.hitbox_offsets[size]
        wd, ht = self.hitbox_dimensions[size]
        self.hitbox = pygame.Rect(
            self.x + offset_x, self.y + offset_y, wd, ht
        )

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

    def update(self):
        # Update movement
        self.x -= self.vel

        # Update hitbox
        offset_x, offset_y = self.hitbox_offsets[self.size]
        wd, ht = self.hitbox_dimensions[self.size]
        self.hitbox = pygame.Rect(
            self.x + offset_x, self.y + offset_y, wd, ht
        )


class SmallCactus:
    hitbox_offset = (1, 1)
    hitbox_dimensions = [
        (14, 16),
        (30, 16),
        (46, 16)
    ]

    def __init__(self, size, add_x):
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/small_cactus.png")
        images = clip_set_to_list_on_xaxis(spriteset)
        self.image = images[size]
        self.dimensions = self.image.get_size()
        self.size = size

        self.x = (add_x * 16) + 256
        self.y = 95
        self.vel = 1

        offset_x, offset_y = self.hitbox_offset
        wd, ht = self.hitbox_dimensions[size]
        self.hitbox = pygame.Rect(
            self.x + offset_x, self.y + offset_y, wd, ht
        )

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.vel

        # Update hitbox
        offset_x, offset_y = self.hitbox_offset
        wd, ht = self.hitbox_dimensions[self.size]
        self.hitbox = pygame.Rect(
            self.x + offset_x, self.y + offset_y, wd, ht
        )


class Bird:
    hitbox_offset = (2, 1)
    hitbox_dimensions = (13, 9)

    def __init__(self, height, add_x):
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/bird.png")
        self.images = clip_set_to_list_on_xaxis(spriteset)
        self.idx = 0

        self.dimensions = self.images[0].get_size()

        self.x = (add_x * 16) + 256
        self.y = (16 * (4 + height)) + 2
        self.vel = 1

        offset_x, offset_y = self.hitbox_offset
        wd, ht = self.hitbox_dimensions
        self.hitbox = pygame.Rect(
            self.x + offset_x, self.y + offset_y, wd, ht
        )

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

        # Update hitbox
        offset_x, offset_y = self.hitbox_offset
        wd, ht = self.hitbox_dimensions
        self.hitbox = pygame.Rect(
            self.x + offset_x, self.y + offset_y, wd, ht
        )