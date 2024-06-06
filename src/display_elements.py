from functions import clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class MenuTitle:
    def __init__(self):
        animation_set = pygame.image.load(
            f"{resources_path}/titles/menu.png")
        self.idx = 0

        # Frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Initialize
            img_rect = pygame.Rect(
                (0, 0), img.get_size())
            
            # Resize
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)

            # Append
            frame = [img, img_rect]
            self.frames.append(frame)

    def draw(self, display):
        # Draw
        img, rect = self.frames[self.idx]
        display.blit(img, rect)

        # Update
        if self.idx < len(self.frames) - 1:
            self.idx += 1