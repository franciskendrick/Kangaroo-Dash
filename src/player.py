from functions import clip_set_to_list_on_xaxis
from window import window
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Player:
    def __init__(self):
        # Movement
        self.x, self.y = (32, 87)
        self.speed_constant = 0.5
        self.t = 0

        # Sprite
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/kangaroo.png")
        self.idx = 0

        # Images 
        self.images = [img for img in clip_set_to_list_on_xaxis(spriteset)]

        # Action
        self.actions = {
            "run": True,
            "jump": False,
            "duck": False
        }

    # Draw
    def draw(self, display):
        # Delta multiplier
        dt = round(window.delta_time)
        dt_multiplier = round(8 / dt) if dt > 0 else 0
        multiplier = dt_multiplier if dt_multiplier > 0 else 8
        
        # Update frame
        if self.idx >= len(self.images) * multiplier:
            self.idx = 0

        # Draw
        img = self.images[self.idx // multiplier]
        display.blit(img, (self.x, self.y))

        # Update frame
        self.idx += 1

    # Actions
    def run(self):
        self.actions = {
            "run": True,
            "jump": False,
            "duck": False
        }

    def jump(self):
        self.actions = {
            "run": False,
            "jump": True,
            "duck": False
        }

    # Update
    def update(self):
        if self.actions["jump"]:
            y = (23/50) * ((self.t - 10) ** 2) + 41
            self.y = y
            self.t += self.speed_constant

            if self.y > 87 or self.t >= 21:
                self.t = 0
                self.y = 87
                self.actions = {
                    "run": True,
                    "jump": False,
                    "duck": False
                }
