from window import window, Background, Middleground, Foreground, Floor
from display_elements import MenuTitle, GameoverTitle, Tutorial, Score
from obstacles import BigCactus, SmallCactus, Bird
from audio import Music, SoundSFX
from player import Player
import pygame
import random
import sys


# Redraw
def redraw_menu():
    # Draw backgrounds and floor
    for bg in bg_layers:
        bg.draw(display)
    floor.draw(display)

    # Draw display elements
    menu_title.draw(display)
    tutorial.draw(display)
    score.draw(display)

    # Draw entities
    player.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_game():
    # Draw backgrounds 
    for bg in bg_layers:
        bg.draw(display)

    # Draw entities
    player.draw(display)
    for obstacle in obstacles:
        obstacle.draw(display)

    # Draw floor
    floor.draw(display)

    # Draw display elements
    score.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_gameover():
    # Draw backgrounds and floor
    for bg in bg_layers:
        bg.draw(display)
    floor.draw(display)

    # Draw entities
    player.draw(display)
    for obstacle in obstacles:
        obstacle.draw(display)

    # Draw display elements
    gameover_title.draw(display)
    tutorial.draw(display)
    score.draw(display) 

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loops
def menu_loop(): 
    run = True
    while run:
        # Update delta time 
        window.update_deltatime()

        # Get game events
        for event in pygame.event.get():
            # Check if user closed the game window
            if event.type == pygame.QUIT:
                run = False

            # Check if a key has been pressed
            if event.type == pygame.KEYDOWN:
                # Check if the menu title animation has finished
                if menu_title.idx >= 14 * 6:
                    # Jump key
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        soundsfx.play_jump()
                        player.jump()
                        game_loop()
                    # Duck key
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.duck()
                        game_loop()
                
                # Toggle sound effects
                if event.key == pygame.K_n:
                    soundsfx.playing = not soundsfx.playing
                # Toggle music
                elif event.key == pygame.K_m:
                    music.playing = not music.playing
                    music.update()

        # Redraw
        redraw_menu()

        # Framerate
        clock.tick(window.framerate)

    # Update highscore file when the loop ends
    score.update_highscore_file()

    # Exit program
    pygame.quit()
    sys.exit()


def game_loop():
    # Unpase entities
    for obstacle in obstacles:
        obstacle.pause = False
    player.pause = False
    player.update_multiplier(obs_velocity)

    # Reset score to zero
    score.score = 0

    run = True
    collision = False
    while run:
        # Update delta time 
        window.update_deltatime()

        # Check game events
        for event in pygame.event.get():
            # Check if user closed the game window
            if event.type == pygame.QUIT:
                run = False

            # Check if a key has been released
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and player.action == "duck":
                    player.run()

            # Check if a key has been pressed
            if event.type == pygame.KEYDOWN:
                # Toggle sound effects
                if event.key == pygame.K_n:
                    soundsfx.playing = not soundsfx.playing
                # Toggle music
                elif event.key == pygame.K_m:
                    music.playing = not music.playing
                    music.update()

        # Check if a key has been pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if player.action != "jump":
                soundsfx.play_jump()
            player.jump()
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.action != "jump":
            player.duck()

        # Update player
        player.update()

        # Update obstacles
        removing_obstacles = []
        for obstacle in obstacles:
            # Update obstacle movement
            obstacle.update()

            # Check for player and obstacle collision 
            player_hitboxes = player.get_hitboxes()
            for hitbox in player_hitboxes:
                if hitbox.colliderect(obstacle.hitbox):
                    collision = True
                    obstacle_hit_type = type(obstacle)

            # If obstacle is out of the screen
            if obstacle.x + obstacle.dimensions[0] <= 0:
                # Add obstacle to list of obstacles being removed
                removing_obstacles.append(obstacle)
                
                # Add new obstacle
                add_x = (obstacles[-1].x // 16) - random.randint(1, 7)
                new_obstacle = random.choice([BigCactus, SmallCactus, Bird])
                obstacles.append(
                    new_obstacle(random.randint(0, 2), add_x, obs_velocity)
                )

        # Pops obstacles that are out of the screen
        for obstacle in removing_obstacles:
            obstacles.pop(obstacles.index(obstacle))

        # Update background movement
        moving_layers = [floor, bg_layers[2], bg_layers[1]]
        for layer, vel in zip(moving_layers, bg_velocities):
            layer.move(vel)

        # Update score
        score.score += 0.25

        if obs_velocity < 8.5:
            # Update obstacle velocity
            update_obsvelocity(score.score)

            # Update player
            player.update_gravityconstant(obs_velocity)
            player.update_multiplier(obs_velocity)

            # Calibrate background velocities
            calibrate_bgvelocites()

            # Calibrate obstacles' velocities
            for obstacle in obstacles:
                obstacle.vel = obs_velocity

        # Redraw
        redraw_game()

        # Framerate
        clock.tick(window.framerate)

        # Check if player lost
        if collision:
            if obstacle_hit_type == BigCactus or obstacle_hit_type == SmallCactus:
                soundsfx.play_cactuscollide()
            elif obstacle_hit_type == Bird:
                soundsfx.play_birdcollide()

            gameover_loop()

    # Update highscore file when the loop ends
    score.update_highscore_file()

    # Exit program
    pygame.quit()
    sys.exit()


def gameover_loop():
    # Pause entities
    for obstacle in obstacles:
        obstacle.pause = True
    player.pause = True

    # Update highscore if current score is higher
    if score.score > score.highscore:
        score.highscore = round(score.score)

    run = True
    while run:
        # Update delta time
        window.update_deltatime()

        # Check game events
        for event in pygame.event.get():
            # Check if user closed the game window
            if event.type == pygame.QUIT:
                run = False

            # Check if a key has been pressed
            if event.type == pygame.KEYDOWN:
                # Check if the gameover title animation has finished
                if gameover_title.idx >= 13 * 6:
                    # Jump key
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        gameover_title.idx = 0
                        player.jump()
                        init_entities()
                        game_loop()
                    # Duck key
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        gameover_title.idx = 0
                        player.duck()
                        init_entities()
                        game_loop()

                # Toggle sound effects
                if event.key == pygame.K_n:
                    soundsfx.playing = not soundsfx.playing
                # Toggle music
                elif event.key == pygame.K_m:
                    music.playing = not music.playing
                    music.update()

        # Redraw
        redraw_gameover()

        # Framerate
        clock.tick(window.framerate)

    # Update highscore file when the loop ends
    score.update_highscore_file()

    # Exit program
    pygame.quit()
    sys.exit()


# Math functions
def get_next_score_threshold(idx):
    return round((41.07016289 * (1.02264021 ** idx)))  # exponential equation: 41.07016289 * 1.02264021^x


# Initialization functions
def init_entities():
    global player, obstacles, obs_velocity

    # Initialize obstacle velocity
    obs_velocity = 2

    # Initialize player
    player = Player(obs_velocity)

    # Initialize obstacles
    obstacles = []
    add_x = 0
    for _ in range(3):
        obstacle = random.choice([BigCactus, SmallCactus, Bird])
        add_x = add_x if add_x == 0 else add_x - random.randint(1, 5)

        obstacles.append(
            obstacle(random.randint(0, 2), add_x, obs_velocity)
        )

        add_x += 16


def calibrate_bgvelocites():
    global bg_velocities

    velocity_ratio = [3, 1, 0.25]  # velocity ratio: 3 : 1 : 0.25

    bg_velocities = [
        obs_velocity,  # floor velocity
        obs_velocity * (velocity_ratio[1] / velocity_ratio[0]),  # foreground velocity
        obs_velocity * (velocity_ratio[2] / velocity_ratio[0])  # middleground velocity
    ]


# Update functions
def update_obsvelocity(score):
    global obs_velocity, next_score_threshold, score_threshold_idx

    if next_score_threshold <= score:
        next_score_threshold += get_next_score_threshold(score_threshold_idx)

        obs_velocity += 0.1
        obs_velocity = round(obs_velocity, 1)

        score_threshold_idx += 1


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
    score = Score()

    # Initialize audio
    music = Music()
    soundsfx = SoundSFX()

    # Initialize entities
    init_entities()
    score_threshold_idx = 0
    next_score_threshold = get_next_score_threshold(score_threshold_idx)

    # Calibrate background velocities
    calibrate_bgvelocites()
    
    # Run the game
    menu_loop()