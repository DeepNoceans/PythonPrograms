import pygame
import sys
import random

from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((1000, 875))

pygame.display.set_caption("DVD Bounce")



pos_x = 250
pos_y = 218.75
vel_x = .25
vel_y = .25
color = 255, 255, 0

counter = 0

screenR = 0
screenG = 0
screenB = 100
RGBcycle = 3

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    
    #MOVE THE RECTANGLE
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 900 or pos_x < 0:
        vel_x = -vel_x
        color = random.randint(30, 255), random.randint(30, 255), random.randint(30, 255)

    if pos_y > 775 or pos_y < 0:
        vel_y = -vel_y
        color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)

    
    screen.fill((screenR, screenG, screenB))

    pos = pos_x, pos_y, 100, 100
    width = 0

    F1pos_x = pos_x - 5
    F1pos_y = pos_y - 5

    Frame1pos = F1pos_x, F1pos_y, 110, 110

    Frame1color = (20,20,20)
    pygame.draw.rect(screen, Frame1color, Frame1pos, width)



    pygame.draw.rect(screen, color, pos, width)


    



    
    T1color = 0,0,0
    myfont = pygame.font.Font(None, 50)

    textImage = myfont.render("DVD", True, T1color)

    DVDpos_x = pos_x + 14
    DVDpos_y = pos_y + 25
    screen.blit(textImage, (DVDpos_x, DVDpos_y))

    
    E1color = (0,0,0)

    E1pos_x = pos_x + 10
    E1pos_y = pos_y + 60
    E1rect = E1pos_x, E1pos_y, 80, 27

    pygame.draw.ellipse(screen, E1color, E1rect, width=0)

    E2pos_x = pos_x + 37
    E2pos_y = pos_y + 70

    E2rect = (E2pos_x, E2pos_y, 27, 7)
    color2 = 255, 255, 255
    pygame.draw.ellipse(screen, color, E2rect, width=0)

    counter += 1

    if counter == 10:
        counter = 0
        if RGBcycle == 1:
            screenR += 1
            screenG -= 1
            screenB -= 1
        
        elif RGBcycle == 2:
            screenR -= 1
            screenG += 1
            screenB -= 1

        elif RGBcycle == 3:
            screenR -= 1
            screenG -= 1
            screenB += 1


        if screenR == 254 or screenG == 254 or screenB == 254:
            RGBcycle +=1
            if RGBcycle == 4:
                RGBcycle = 1
        
        if screenR <= 50:
            screenR += 1
        
        if screenG <= 50:
            screenG += 1
        
        if screenB <= 50:
            screenB += 1


    pygame.display.update()
