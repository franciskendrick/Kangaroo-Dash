from window import window, Background
from display_elements import MenuTitle
import pygame
import sys


def redraw():
    background.draw(display)
    menu_title.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # TEMPORARY !!!
        import time
        time.sleep(0.1)
        redraw()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Initialize pygame window
    win_size = (
        int(window.rect.width * window.enlarge),
        int(window.rect.height * window.enlarge))
    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(window.rect.size)

    # Initialize window objects
    background = Background()
    menu_title = MenuTitle()

    loop()