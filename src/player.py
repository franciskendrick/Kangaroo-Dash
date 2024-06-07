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
        spriteset = pygame.image.load(
            f"{resources_path}/sprites/kangaroo.png")
        self.idx = 0

        # Frames 
        self.frames = []
        for img in clip_set_to_list_on_xaxis(spriteset):
            # Initialize
            wd, ht = img.get_size()
            img_rect = pygame.Rect(
                (32, 112 - ht), (wd, ht))
            
            # Append 
            frame = [img, img_rect]
            self.frames.append(frame)

    def draw(self, display):
        # Delta multiplier
        dt = round(window.delta_time)
        dt_multiplier = round(8 / dt) if dt > 0 else 0
        multiplier = dt_multiplier if dt_multiplier > 0 else 8
        
        # Update frame
        if self.idx >= len(self.frames) * multiplier:
            self.idx = 0

        # Draw
        img, rect = self.frames[self.idx // multiplier]
        display.blit(img, rect)

        # Update frame
        self.idx += 1
