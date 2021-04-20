import pygame
import random
from pygame.locals import *
import sys
pygame.init()


screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Ellipse")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill((20,20,20))




    E1color = (255, 140, 0)

    E1rect = (320, 350, 50, 300)


    pygame.draw.ellipse(screen, E1color, E1rect, width=0)



    E2color = (30, 144, 255)

    E2rect = (620, 350, 50, 300)

    pygame.draw.ellipse(screen, E2color, E2rect, width=0)


    C1color = (255,255,255)
    C1origin = (500,400)
    C1radius = 40
    pygame.draw.circle(screen, C1color, C1origin, C1radius, width=0)

    
    


    pygame.display.update()
