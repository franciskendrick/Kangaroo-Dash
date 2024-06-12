from window import window, Background, Middleground, Foreground, Floor
from display_elements import MenuTitle, GameoverTitle, Tutorial
from obstacles import BigCactus, SmallCactus, Bird
from player import Player
import pygame
import random
import sys


# Redraw
def redraw_menu():
    for bg in bg_layers:
        bg.draw(display)
    floor.draw(display)

    menu_title.draw(display)
    tutorial.draw(display)

    player.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_game():
    for bg in bg_layers:
        bg.draw(display)

    player.draw(display)
    for obstacle in obstacles:
        obstacle.draw(display)

    floor.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_gameover():
    for bg in bg_layers:
        bg.draw(display)
    floor.draw(display)

    player.draw(display)
    for obstacle in obstacles:
        obstacle.draw(display)

    gameover_title.draw(display)
    tutorial.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loops
def menu_loop(): 
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.jump()
                    game_loop()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.duck()
                    game_loop()

        redraw_menu()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def game_loop():
    for obstacle in obstacles:
        obstacle.pause = False
    player.pause = False

    run = True
    collision = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and player.action == "duck":
                    player.run()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.jump()
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.action != "jump":
            player.duck()

        # Update player
        player.update()

        # Update obstacles
        removing_obstacles = []
        for obstacle in obstacles:
            # Update movement
            obstacle.update()

            # Collision detection
            player_hitboxes = player.get_hitboxes()
            for hitbox in player_hitboxes:
                if hitbox.colliderect(obstacle.hitbox):
                    collision = True

            # Update obstacles on screen
            if obstacle.x + obstacle.dimensions[0] <= 0:
                removing_obstacles.append(obstacle)
                
                add_x = (obstacles[-1].x // 16) - random.randint(1, 7)
                new_obstacle = random.choice([BigCactus, SmallCactus, Bird])
                obstacles.append(
                    new_obstacle(random.randint(0, 2), add_x))
                
        for obstacle in removing_obstacles:
            obstacles.pop(obstacles.index(obstacle))

        # Redraw
        redraw_game()
        clock.tick(window.framerate)

        # Check if player lost
        if collision:
            gameover_loop()

    pygame.quit()
    sys.exit()


def gameover_loop():
    for obstacle in obstacles:
        obstacle.pause = True
    player.pause = True

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.jump()
                    init_entities()
                    game_loop()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.duck()
                    init_entities()
                    game_loop()

        redraw_gameover()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


# Initialization functions
def init_entities():
    global player, obstacles

    # Initialize player
    player = Player()

    # Initialize obstacles
    obstacles = []
    add_x = 0
    for _ in range(3):
        obstacle = random.choice([BigCactus, SmallCactus, Bird])
        add_x = add_x if add_x == 0 else add_x - random.randint(1, 5)

        obstacles.append(
            obstacle(random.randint(0, 2), add_x)
        )

        add_x += 16


# Execute
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

    # Initialize background layers
    bg_layers = [Background(), Middleground(), Foreground()]
    floor = Floor()

    # Initialize objects
    menu_title = MenuTitle()
    gameover_title = GameoverTitle()
    tutorial = Tutorial()

    # Initialize entities
    init_entities()
    
    # Run the game
    menu_loop()