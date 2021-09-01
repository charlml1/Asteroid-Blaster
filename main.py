import pygame
import math
import random
from pygame import mixer

# Credits
# Asteroid = Good Ware
# Spaceship = Freepik
# Need to put this whole text paragraph in for the music
#  Corona by Alexander Nakarada | https://www.serpentsoundstudios.com
#  Music promoted by https://www.chosic.com/
#  Attribution 4.0 International (CC BY 4.0)
#  https://creativecommons.org/licenses/by/4.0/

# Start the pygame
pygame.init()
clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Asteroid Blaster")
icon = pygame.image.load('asteroid.png')
pygame.display.set_icon(icon)

# Background Music
mixer.music.load('Corona-320bit.mp3')
mixer.music.play(-1)

# Player
player_image = pygame.image.load("spaceship.png")
player_rect = player_image.get_rect(center = (400,300))
player_X = 380
player_Y = 280
degree = 0

# Bool values for spinning
spin_right = False
spin_left = False

# Bullet
bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect(center = (400,300))
bullet_X = 384
bullet_Y = 284
bullet_degree = 0
fired = False


# Asteroid
asteroid_image = pygame.image.load("asteroid.png")
is_x = random.randint(0,1)
is_start = random.randint(0,1)
asteroid_X = -64
asteroid_Y = -64
if is_x:
    asteroid_X = random.randint(-64,800)
    if not is_start:
        asteroid_Y = 600
else:
    asteroid_Y = random.randint(-64, 600)
    if not is_start:
        asteroid_X = 800

# Game Over
end_font = pygame.font.Font('DassaultTitle-22mv.otf', 90)
game_over = False
play_again_font = pygame.font.Font('DassaultTitle-22mv.otf', 32)

# Score
score_font = pygame.font.Font('DassaultTitle-22mv.otf', 38)
score = 0

# Title Screen
title = True
play_font = pygame.font.Font('DassaultTitle-22mv.otf', 70)
big_play_font = pygame.font.Font('DassaultTitle-22mv.otf', 75)
title_font = pygame.font.Font('DassaultTitle-22mv.otf', 110)

# Credit Screen
credit = False
credit_font = pygame.font.Font('freesansbold.ttf', 18)
big_credit_font = pygame.font.Font('freesansbold.ttf', 36)

# Resets asteroid and bullet
def reset():
    global asteroid_X, asteroid_Y, bullet_X, bullet_Y, bullet_degree, fired
    # resets asteroid
    is_x = random.randint(0, 1)
    is_start = random.randint(0, 1)
    asteroid_X = -64
    asteroid_Y = -64
    if is_x:
        asteroid_X = random.randint(-64, 800)
        if not is_start:
            asteroid_Y = 600
    else:
        asteroid_Y = random.randint(-64, 600)
        if not is_start:
            asteroid_X = 800

    # resets bullet
    fired = False
    bullet_X = 384
    bullet_Y = 284
    bullet_degree = 0

# def rotate_player(x, y, degree):
#     global player_image
#     player_image = pygame.transform.rotate(player_image, degree)
#     screen.blit(player_image, (x, y))

# def player(x, y):
#     screen.blit(player_image, (x, y))
#
# def bullet(x,y):
#     screen.blit(bullet_image, (x, y))

# While loop for refreshing the screen
running = True
while running:
    # Choosing screen color
    screen.fill((0,0,0))

    # checking if we're on the title screen or not
    if title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (280 < mouse[0] < 520) and (300 < mouse[1] < 350):
                    title = False
                if (190 < mouse[0] < 600) and (380 < mouse[1] < 425):
                    title = False
                    credit = True
        asteroid_text = title_font.render("Asteroid", True, (255, 255, 125))
        screen.blit(asteroid_text, (20,50))

        blaster_text = title_font.render("Blaster", True, (255, 255, 125))
        screen.blit(blaster_text, (50,130))

        mouse = pygame.mouse.get_pos()
        if (280 < mouse[0] < 520) and (300 < mouse[1] < 345):
            play_text = big_play_font.render("Play", True, (255, 255, 255))
            screen.blit(play_text, (270, 300))
        else:
            play_text = play_font.render("Play", True, (255, 255, 255))
            screen.blit(play_text, (280, 300))

        if (190 < mouse[0] < 600) and (380 < mouse[1] < 425):
            credit_text = big_play_font.render("Credits", True, (255, 255, 255))
            screen.blit(credit_text, (180, 380))
        else:
            credit_text = play_font.render("Credits", True, (255, 255, 255))
            screen.blit(credit_text, (190, 380))


    elif credit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (10 < mouse[0] < 135) and (550 < mouse[1] < 570):
                    title = True
                    credit = False
        credit_title_text = end_font.render("Credits", True, (255, 255, 255))
        screen.blit(credit_title_text, (150, 50))

        # Music credits
        music = big_credit_font.render("Music:", True, (255,255,255))
        music_credits = credit_font.render("Corona by Alexander Nakarada | https://www.serpentsoundstudios.com",
                                           True, (255, 255, 255))
        music_credits2 = credit_font.render("Music promoted by https://www.chosic.com/", True, (255, 255, 255))
        music_credits3 = credit_font.render("Attribution 4.0 International (CC BY 4.0)", True, (255, 255, 255))
        music_credits4 = credit_font.render("https://creativecommons.org/licenses/by/4.0/", True, (255, 255, 255))

        screen.blit(music, (10,150))
        screen.blit(music_credits, (10, 200))
        screen.blit(music_credits2, (10, 220))
        screen.blit(music_credits3, (10, 240))
        screen.blit(music_credits4, (10, 260))

        # Image credits
        images = big_credit_font.render("Images:", True, (255, 255, 255))
        screen.blit(images, (10, 310))

        asteroid_credits = credit_font.render("Asteroid image - Good Ware", True, (255, 255, 255))
        screen.blit(asteroid_credits, (10, 360))

        spaceship_credits = credit_font.render("Spaceship image - Freepik", True, (255, 255, 255))
        screen.blit(spaceship_credits, (10, 380))

        # Back to main menu
        mouse = pygame.mouse.get_pos()
        if (10 < mouse[0] < 135) and (550 < mouse[1] < 570):
            back_text = score_font.render("Back", True, (255, 255, 255))
            screen.blit(back_text, (10, 550))
        else:
            back_text = play_again_font.render("Back", True, (255, 255, 255))
            screen.blit(back_text, (20, 550))
    else:
        # For loop over every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Spinning right and left
                if event.key == pygame.K_RIGHT:
                    spin_right = True
                if event.key == pygame.K_LEFT:
                    spin_left = True
                if event.key == pygame.K_SPACE:
                    # shoots bullet
                    if not fired:
                        fired = True
                        bullet_degree = degree % 360
                        shoot = mixer.Sound("laser_gun.mp3")
                        shoot.set_volume(.3)
                        shoot.play()
                if event.key == pygame.K_x:
                    # resets game after game_over
                    if game_over:
                        game_over = False
                        score = 0
                        reset()
            if event.type == pygame.KEYUP:
                # Stop spinning right or left
                if event.key == pygame.K_RIGHT:
                    spin_right = False
                if event.key == pygame.K_LEFT:
                    spin_left = False

        # checks if the game is still going on
        if not game_over:
            # Spins based on the bool values
            if spin_right:
                degree -= 4
            if spin_left:
                degree += 4
            rotated_image = pygame.transform.rotate(player_image, degree)
            rotated_rect = rotated_image.get_rect()
            rotated_rect.center = player_rect.center

            # Asteroid movement toward the center
            x_difference = 380 - asteroid_X
            y_difference = 280 - asteroid_Y
            total_difference = abs(x_difference) + abs(y_difference)
            asteroid_X += x_difference / (total_difference) * 3
            asteroid_Y += y_difference / (total_difference) * 3

            # Firing the bullet
            if fired:
                rotated_bullet = pygame.transform.rotate(bullet_image, bullet_degree)
                bullet_rect = rotated_bullet.get_rect()
                bullet_rect.center = bullet_rect.center
                if bullet_degree == 0:
                    bullet_Y -= 5
                elif bullet_degree == 90:
                    bullet_X += 5
                elif bullet_degree == 180:
                    bullet_Y += 5
                elif bullet_degree == 270:
                    bullet_X -= 5
                elif bullet_degree < 90:
                    bullet_X -= (bullet_degree/90)*7
                    bullet_Y -= (1- bullet_degree/90)*7
                elif bullet_degree < 180:
                    temp_bullet_degree = bullet_degree - 90
                    bullet_X -= (1 - (temp_bullet_degree / 90)) * 7
                    bullet_Y += (temp_bullet_degree / 90) * 7
                elif bullet_degree < 270:
                    temp_bullet_degree = bullet_degree - 180
                    bullet_X += (temp_bullet_degree / 90) * 7
                    bullet_Y += (1 - (temp_bullet_degree / 90)) * 7
                elif bullet_degree < 360:
                    temp_bullet_degree = bullet_degree - 270
                    bullet_X += (1-(temp_bullet_degree / 90)) * 7
                    bullet_Y -= (temp_bullet_degree / 90) * 7
                screen.blit(rotated_bullet, (bullet_X, bullet_Y))

            # finding the center of the asteroid
            temp_asteroid_center = asteroid_image.get_rect().center
            asteroid_center = [0, 0]
            asteroid_center[0] = temp_asteroid_center[0] + asteroid_X
            asteroid_center[1] = temp_asteroid_center[1] + asteroid_Y

            # Checking if bullet hit asteroid
            temp_bullet_center = bullet_image.get_rect().center
            bullet_center = [0, 0]
            bullet_center[0] = temp_bullet_center[0] + bullet_X
            bullet_center[1] = temp_bullet_center[1] + bullet_Y
            bullet_distance = math.sqrt((asteroid_center[0] - bullet_center[0]) ** 2 +
                                        (asteroid_center[1] - bullet_center[1]) ** 2)
            if bullet_distance < 30:
                reset()

                # changes score
                score += 1

            if bullet_X > 800 or bullet_X < 0 or bullet_Y < 0 or bullet_Y > 600:
                fired = False
                bullet_X = 384
                bullet_Y = 284

        # Show Player
        screen.blit(rotated_image, rotated_rect)

        # Show Asteroid
        screen.blit(asteroid_image, (asteroid_X, asteroid_Y))

        # Show Score
        score_text = score_font.render("Score: {}".format(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # distance between player and asteroid
        player_distance = math.sqrt((asteroid_center[0] - 400) ** 2 + (asteroid_center[1] - 300) ** 2)

        # game over if asteroid hit the player
        if player_distance < 50:
            end_text = end_font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(end_text, (50, 250))
            game_over = True

            play_again_text = play_again_font.render("(Press x to play again)", True, (255, 255, 255))
            screen.blit(play_again_text, (140, 320))

    # keeps at a certain fps
    clock.tick(60)

    # Updates the screen
    pygame.display.update()

