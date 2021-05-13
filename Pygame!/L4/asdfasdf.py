
import pygame
import random
from pygame.locals import *
import sys
pygame.init()


screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Wierd Polygon")


pos_x = 500

pos_y = 450

radius = 200

angle = 360

wide = 40

color = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((20, 20, 20))


    pos = (int(pos_x), int(pos_y)), (int(pos_x)+200,
                                            int(pos_y)-320), (int(pos_x)-40, int(pos_y)-40), (int(pos_x)+400, int(pos_y)+300), (int(pos_x)-500, int(pos_y)-100)

    pygame.draw.polygon(screen, color, pos, 1)
    pygame.display.update()
