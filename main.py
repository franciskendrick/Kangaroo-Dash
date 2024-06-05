from window import window
import pygame
import sys


def redraw():
    pygame.display.update()


def loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redraw()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Intialize pygame window
    win_size = (
        int(window.rect.width * window.enlarge),
        int(window.rect.height * window.enlarge))
    win = pygame.display.set_mode(win_size)

    loop()
