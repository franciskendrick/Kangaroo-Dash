from window import window, Background
from display_elements import MenuTitle, Tutorial
from player import Player
import pygame
import sys


def redraw_menu():
    background.draw(display)
    menu_title.draw(display)
    tutorial.draw(display)
    player.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_game():
    background.draw(display)
    player.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def menu_loop(): 
    run = True
    while run:
        window.update_deltatime()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redraw_menu()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def game_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.jump()

        player.update()

        redraw_game()
        clock.tick(window.framerate)

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
    pygame.display.set_caption("Kangaroo Dash")
    clock = pygame.time.Clock()

    # Initialize objects
    background = Background()
    menu_title = MenuTitle()
    tutorial = Tutorial()

    player = Player()

    # Run the game
    # menu_loop()
    game_loop()  # TEMPORARY !!!