# Mohamad Moussaoui


import sys
import random
import time
import pygame
from pygame.locals import *


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

#what the bruh is this
#main program begins
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Bomb Catching Game 2 ")
font1 = pygame.font.Font(None, 30)
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
white = 255, 255, 255
red = 220, 50, 50
yellow = 230, 230, 50
black = 0, 0, 0

orange = 255, 120, 0

cyan = 0, 255, 255
purple = 255, 0, 255
green = 0, 255, 0

lives = 5
score = 0
clock_start = 0
game_over = True
mouse_x = mouse_y = 0

pos_x = 250
pos_y = 765

bomb_x =  random.randint(30, 970)
bomb_x1 = random.randint(30, 970)
bomb_x2 = random.randint(30, 970)
bomb_x3 = random.randint(30, 970)
bomb_x4 = random.randint(30, 970)

# bomb_x = 250
# bomb_x1 =250
# bomb_x2 =250
# bomb_x3 =250
# bomb_x4 =250



bomb_y = -200
bomb_y1 = -400
bomb_y2 = -600
bomb_y3 = -800

bomb_y4 = -1000
bomb_y5 = -2000


vel_y = .6
vel_x = 1
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
                lives = 5
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    if game_over:
        print_text(font1, 100, 200, "<CLICK TO PLAY>")

        bomb_y = -200
        bomb_y1 = -400
        bomb_y2 = -600
        bomb_y3 = -800

        bomb_y4 = -1000

        bomb_y5 = -1000
        bomb_x5 = random.randint(2, 990)
        
    else:
        #move the bomb
        bomb_y += vel_y
        bomb_y1 += vel_y
        bomb_y2 += vel_y
        bomb_y3 += vel_y
        bomb_y4 += (vel_y/4)
        bomb_y5 += (vel_y/6)
        bomb_x5 += vel_x

        if bomb_x5 > 980 or bomb_x5 < 20:
            vel_x = -vel_x
        #    0

        #has the player missed the bomb?
        if bomb_y > 800:
            bomb_x = random.randint(30, 970)
            # bomb_x = 250

            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10

                bomb_x = random.randint(30, 970)
                # bomb_x = 250

                bomb_y = -50



        #     1

        if bomb_y1 > 800:
            bomb_x1 = random.randint(30, 970)
            # bomb_x1 = 250

            bomb_y1 = -50
            

            lives -= 1
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y1 > pos_y:
            if bomb_x1 > pos_x and bomb_x1 < pos_x + 120:
                score += 10

                bomb_x1 = random.randint(30, 970)
                # bomb_x1 = 250

                bomb_y1 = -50


        #     2

        if bomb_y2 > 800:
            bomb_x2 = random.randint(30, 970)
            # bomb_x2 = 250

            bomb_y2 = -50

            lives -= 1
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y2 > pos_y:
            if bomb_x2 > pos_x and bomb_x2 < pos_x + 120:
                score += 10

                bomb_x2 = random.randint(30, 970)
                # bomb_x2 = 250

                bomb_y2 = -50



            #3

        if bomb_y3 > 800:
            bomb_x3 = random.randint(30, 970)
            # # bomb_x3 = 250

            bomb_y3 = -50
            lives -= 1
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y3 > pos_y:
            if bomb_x3 > pos_x and bomb_x3 < pos_x + 120:
                score += 10

                bomb_x3 = random.randint(30, 970)
                # bomb_x3 = 250

                bomb_y3 = -50



         #     4

        if bomb_y4 > 800:
            bomb_x4 = random.randint(250, 750)
            # bomb_x4 = 250

            bomb_y4 = -200
            lives -= 1
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y4 > pos_y - 20:
            if bomb_x4 > pos_x and bomb_x4 < pos_x + 120:
                score += 20

                bomb_x4 = random.randint(250, 750)
                # bomb_x4 = 250

                bomb_y4 = -200

         #     5

        if bomb_y5 > 800:
            bomb_x5 = random.randint(0, 1000)
            # bomb_x5 = 250

            bomb_y5 = -1000
           
            if lives == 1:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y5 > pos_y - 20:
            if bomb_x5 > pos_x and bomb_x5 < pos_x + 120:
                score += 100

                bomb_x5 = random.randint(0, 1000)
                # bomb_x5 = 250

                bomb_y5 = -2000


        # draw the bomb
        pygame.draw.circle(screen, black, (bomb_x-4, int(bomb_y)-4), 30, 0)
        pygame.draw.circle(screen, yellow, (bomb_x, int(bomb_y)), 30, 0)
        pygame.draw.circle(screen, black, (bomb_x1-4, int(bomb_y1)-4), 30, 0)
        pygame.draw.circle(screen, red, (bomb_x1, int(bomb_y1)), 30, 0)
        pygame.draw.circle(screen, black, (bomb_x2-4, int(bomb_y2)-4), 30, 0)
        pygame.draw.circle(screen, green, (bomb_x2, int(bomb_y2)), 30, 0)
        pygame.draw.circle(screen, black, (bomb_x3-4, int(bomb_y3)-4), 30, 0)
        pygame.draw.circle(screen, cyan, (bomb_x3, int(bomb_y3)), 30, 0)
        pygame.draw.circle(screen, black, (bomb_x4-4, int(bomb_y4)-4), 40, 0)
        pygame.draw.circle(screen, purple, (bomb_x4, int(bomb_y4)), 40, 0)
        pygame.draw.circle(screen, black, (bomb_x5-4, int(bomb_y5)-4), 20, 0)
        pygame.draw.circle(screen, orange, (bomb_x5, int(bomb_y5)), 20, 0)
        #set basket position
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 880:
            pos_x = 880
        #draw basket
        pygame.draw.rect(screen, black, (pos_x-4, pos_y-4, 120, 40), 0)
        pygame.draw.rect(screen, red, (pos_x, pos_y, 120, 40), 0)

    #print # of lives
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    print_text(font1, 850, 0, "SCORE: " + str(score))

    pygame.display.update()
