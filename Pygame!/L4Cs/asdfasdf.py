
import pygame
import random
from pygame.locals import *
import sys
pygame.init()


screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Ellipse")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((20, 20, 20))




    pos = (int(pos_x + x), int(pos_y + y)), (int(pos_x + x)+20,
                                            int(pos_y + y)+20), (int(pos_x + x)-40, int(pos_y + y)-40), (int(pos_x + x)+100, int(pos_y + y)-10)

    pygame.draw.polygon(screen, color, pos, 0)
    pygame.display.update()
