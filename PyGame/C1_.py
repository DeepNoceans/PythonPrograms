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

        screen.fill((100, 120, 150))


        color = 255, 255, 255
        pos = 500, 500, 100, 100
        width = 0
        rect = (500, 500, 100, 100)


        pygame.draw.ellipse(screen, color, rect, width=0)
