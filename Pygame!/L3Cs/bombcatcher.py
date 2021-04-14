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

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


#main program begins
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

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

vel_x = random.randint(-3, 3)
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

    if game_over:
        print_text(font1, 100, 200, "<CLICK TO PLAY>")
    else:
        #move the bomb
        bomb_y += vel_y

        bomb_x += vel_x

        if bomb_x > 1470 or bomb_x < 30:
            vel_x = -vel_x

  
        #has the player missed the bomb?
        if bomb_y > 1000:
            bomb_x = random.randint(100, 1400)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
            mixer.music.play()
            vel_x = random.randint(-3, 3)


        #see if player has caught the bomb
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 200:
                score += 10
                bomb_x = random.randint(100, 1400)
                bomb_y = -50
                vel_x = random.randint(-3, 3)

        #draw the bomb
        pygame.draw.circle(screen, black, (bomb_x-2, int(bomb_y)-2), 40, 0)
        pygame.draw.circle(screen, gray, (bomb_x, int(bomb_y)), 40, 0)


        fuse_pos1 = bomb_x, bomb_y - 40
        fuse_pos2 = bomb_x + 10, bomb_y - 60
    
        
        pygame.draw.line(screen, white, fuse_pos1, fuse_pos2, 4)


       
        
        for i in range(0, 25):


            color = random.randint(150, 255), random.randint(
                0, 100), random.randint(0, 100),

            spark_pos1 = fuse_pos2 
 
            spark_pos2 = bomb_x + 10 + random.randint(-5, 5), bomb_y - 60 + random.randint(-5, 5)

            spark_width = 5

            pygame.draw.line(screen, color, spark_pos1, spark_pos2, spark_width)

        for i in range(0, 5):

            color = random.randint(150, 255), random.randint(
                0, 100), random.randint(0, 100),

            spark_pos1 = fuse_pos2

            spark_pos2 = bomb_x + 10 + random.randint(-10, 10), bomb_y - 60 + random.randint(-10, 10)

            spark_width = 5

            pygame.draw.line(screen, color, spark_pos1, spark_pos2, spark_width)
            #set basket position

        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 1400:
            pos_x = 1400
        #draw basket
        pygame.draw.rect(screen, black, (pos_x-2, pos_y-2, 200, 40), 0)
        pygame.draw.rect(screen, red, (pos_x, pos_y, 200, 40), 0)

    #print # of lives
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    print_text(font1, 1400, 0, "SCORE: " + str(score))

    pygame.display.update()

