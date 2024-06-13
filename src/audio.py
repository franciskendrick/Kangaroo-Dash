import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class SoundSFX:
    def __init__(self):
        self.jump = pygame.mixer.Sound(
            f"{resources_path}/audio/ES_Boots Jump.mp3")
        self.cactus_collide = pygame.mixer.Sound(
            f"{resources_path}/audio/ES_Grass Pull.mp3")
        self.bird_collide = pygame.mixer.Sound(
            f"{resources_path}/audio/ES_Raven Squawk.mp3")
        
        self.playing = True
    
    def play_jump(self):
        if self.playing:
            self.jump.play()

    def play_cactuscollide(self):
        if self.playing:
            self.cactus_collide.play()

    def play_birdcollide(self):
        if self.playing:
            self.bird_collide.play()


class Music:
    def __init__(self):
        pygame.mixer.music.load(
            f"{resources_path}/audio/ES_Dreamz - Jerry Lacey.mp3")
        pygame.mixer.music.set_volume(0.5)

        pygame.mixer.music.play(-1)
        self.playing = True

    def update(self):
        if self.playing:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()