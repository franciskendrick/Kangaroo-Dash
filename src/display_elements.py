from functions import clip_font_to_dict, clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Title:
    def init(self, filename, x, y):
        animation_set = pygame.image.load(
            f"{resources_path}/display_elements/{filename}.png")
        self.idx = 0

        # Initialize frames
        self.frames = []
        self.shadows = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Initialize rectangles 
            img_rect = pygame.Rect(
                (x, y), img.get_size())
            shadow_rect = pygame.Rect(
                (x - 2, y + 1), img.get_size())
            
            # Resize image
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


class NumberFont:
    def __init__(self):
        font_set = pygame.image.load(
            f"{resources_path}/display_elements/numberfont.png")
        self.order = [
            "0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9",
            ","
        ]

        self.characters = clip_font_to_dict(
            font_set, self.order)
        
        # Spacing
        self.character_spacing = 1
        self.space = 3

    def render_font(self, display, text, pos):
        display_handle = pygame.Surface(
            display.get_size(), pygame.SRCALPHA)
        x, y = pos
        x_offset = 0

        # Loop over every character in text
        for char in text:
            if char != " ":  # if character
                # Get character image
                character = self.characters[char]
            
                # Blit to handle display
                display_handle.blit(character, (x + x_offset, y))

                # Add to offset: character width + spacing
                x_offset += character.get_width() + self.character_spacing
            else:  # if space
                # Add to offset: space width + spacing
                x_offset += self.space + self.character_spacing

        # Blit to actual display
        display.blit(display_handle, (0, 0))

    def get_fontsize(self, text):
        wd = 0
        heights = []

        # Loop over every character in text
        for char in text:
            if char != " ":  # if character
                # Get character image
                character = self.characters[char]

                # Add to width: character width + spacing
                wd += character.get_width() + self.character_spacing

                # Append character's height
                heights.append(character.get_height())
            else:  # if space
                # Add to width: space width + spacing
                x_offset += self.space + self.character_spacing

        # Return font size
        return (wd, max(heights))


class MenuTitle(Title):
    def __init__(self):
        super().__init__()

        self.init("menu", 0, 0)


class GameoverTitle(Title):
    def __init__(self):
        super().__init__()
        
        self.init("gameover", 38, 0)


class Tutorial:
    def __init__(self):
        spriteset = pygame.image.load(
            f"{resources_path}/display_elements/tutorial.png")
        self.idx = 0

        # Initialize frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(spriteset):
            # Initialize rectangle
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


class Score(NumberFont):
    def __init__(self):
        super().__init__()

        # Highscore label
        self.hs_image = pygame.image.load(
            f"{resources_path}/display_elements/highscore.png")

        # Get highscore file
        highscore_file = open(f"{resources_path}/highscore.txt", "r")

        # Data
        self.score = 0
        self.highscore = int(highscore_file.read())

    def draw(self, display):
        # Draw highscore
        display.blit(self.hs_image, (1, 1))

        highscore = f"{round(self.highscore):,}"
        self.render_font(display, highscore, (16, 1))

        # Draw current score
        score = f"{round(self.score):,}"
        wd, _ = self.get_fontsize(score)
        self.render_font(display, score, (256 - wd, 1))

    def update_highscore_file(self):
        highscore_file = open(f"{resources_path}/highscore.txt", "w")
        highscore_file.write(str(self.highscore))
