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
        self.shadows = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Initialize
            img_rect = pygame.Rect(
                (0, 0), img.get_size())
            shadow_rect = pygame.Rect(
                (-2, 1), img.get_size())
            
            # Resize
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)

            # Set shadows to transparent
            shadow_img = img.copy()
            shadow_img.set_alpha(100)
            
            # Append
            frame = [img, img_rect]
            shadow = [shadow_img, shadow_rect]
            self.frames.append(frame)
            self.shadows.append(shadow)

    def draw(self, display):
        # Draw
        img, rect = self.shadows[self.idx // 6]
        display.blit(img, rect)

        img, rect = self.frames[self.idx // 6]
        display.blit(img, rect)

        # Update frame
        if self.idx < (len(self.frames) - 1) * 6:
            self.idx += 1


class Tutorial:
    def __init__(self):
        spriteset = pygame.image.load(
            f"{resources_path}/titles/tutorial.png")
        self.idx = 0

        # Frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(spriteset):
            # Initialize
            img_rect = pygame.Rect(
                (67, 81), img.get_size())
            
            # Append
            frame = [img, img_rect]
            self.frames.append(frame)

    def draw(self, display):
        # Update frame
        if self.idx >= len(self.frames) * 8:
            self.idx = 0
        
        # Draw
        img, rect = self.frames[self.idx // 8]
        display.blit(img, rect)

        # Update frame
        self.idx += 1