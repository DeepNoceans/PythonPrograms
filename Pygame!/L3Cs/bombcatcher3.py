# Bomb Catcher Game

import sys
import random
import time
import pygame
from pygame.locals import *
from pygame import mixer
mixer.init()

# Loading the song
mixer.music.load("boom.wav")

# Setting the volume

# Start playing the song


def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


#main program begins
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
bomb_bird = pygame.image.load("bomb_bird.png").convert_alpha()
bomb_bird = pygame.transform.scale(bomb_bird,(100, 120))
WP1 = pygame.image.load("WP_angry_birds1.jpg").convert_alpha()
WP1 = pygame.transform.scale(WP1, (1500, 1000))

white = 255, 255, 255
red = 220, 50, 50
yellow = 230, 230, 50
black = 0, 0, 0
gray = 40, 40, 40

lives = 3
score = 0
clock_start = 0
game_over = True
mouse_x = mouse_y = 0

pos_x = 300
pos_y = 970

bomb_x = random.randint(100, 1400)
bomb_y = -50


vel_y = 3
# vel_x = random.randint(-3, 3)
vel_x = 0



#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            move_x, move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((100, 100, 200))
    screen.blit(WP1, (0,0))

    print_text(font1, 1400, 0, "SCORE: " + str(score))

    if game_over:
        print_text(font1, 100, 200, "<CLICK TO PLAY>")
    else:

        #print # of lives
        print_text(font1, 0, 0, "LIVES: " + str(lives))

        #print score

        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 1400:
            pos_x = 1400
        #draw basket
        pygame.draw.rect(screen, black, (pos_x-2, pos_y-2, 200, 40), 0)
        pygame.draw.rect(screen, red, (pos_x, pos_y, 200, 40), 0)
        #move the bomb
        bomb_y += vel_y

        bomb_x += vel_x

        if bomb_x > 1470 or bomb_x < 30:
            vel_x = -vel_x

        #has the player missed the bomb?
        if bomb_y > 1000:
            lives -= 1
            if lives == 0:
                game_over = True
            mixer.music.play()
            vel_x = random.randint(-3, 3)

            myfont = pygame.font.Font(None, 41)

            textImage = myfont.render("boom", True, black)

            screen.blit(textImage, (bomb_x, 750))

            myfont = pygame.font.Font(None, 40)

            textImage = myfont.render("boom", True, gray)

            screen.blit(textImage, (bomb_x, 750))

            pygame.display.update()

            time.sleep(.5)

            bomb_x = random.randint(100, 1400)
            bomb_y = -50

        #see if player has caught the bomb
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 200:
                score += 10
                bomb_x = random.randint(100, 1400)
                bomb_y = -50
                vel_x = random.randint(-3, 3)

        #draw the bomb
        # pygame.draw.circle(screen, black, (bomb_x-2, int(bomb_y)-2), 40, 0)
        pygame.draw.circle(screen, gray, (bomb_x, int(bomb_y)), 40, 0)
        screen.blit(bomb_bird, (bomb_x-53, int(bomb_y)-77))
       
        
    pygame.display.update()
