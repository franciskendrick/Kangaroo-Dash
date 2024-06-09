from functions import separate_sets_from_yaxis, clip_set_to_list_on_xaxis
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
        spritesets = separate_sets_from_yaxis(
            pygame.image.load(f"{resources_path}/sprites/kangaroo.png"),
            (255, 0, 0))
        
        self.idx = 0
        self.imgtype = "idle"
        self.images = {
            "idle": [img for img in clip_set_to_list_on_xaxis(spritesets[0])],
            "run": [img for img in clip_set_to_list_on_xaxis(spritesets[1])],
            "duck": [img for img in clip_set_to_list_on_xaxis(spritesets[2])]
        }

        # Action
        self.action = "run"

    # Draw
    def draw(self, display):
        images = self.images[self.imgtype]
        y_offset = 12 if self.imgtype == "duck" else 0

        # Update frame
        if self.idx >= len(images) * 8:
            self.idx = 0

        # Draw
        img = images[self.idx // 8]
        display.blit(img, (self.x, self.y + y_offset))

        # Update frame
        self.idx += 1

    # Actions
    def run(self):
        self.action = "run"
        self.imgtype = "run"

    def jump(self):
        self.action = "jump"
        self.imgtype = "run"

    def duck(self):
        self.action = "duck"
        self.imgtype = "duck"

    # Update
    def update(self):
        if self.action == "jump":
            y = (23/50) * ((self.t - 10) ** 2) + 41  # parabola
            self.y = y
            self.t += self.speed_constant

            if self.y > 87 or self.t >= 21:
                self.t = 0
                self.y = 87
                self.run()