import sys
import random
import math
import pygame
from pygame.locals import *


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    # X property

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    # Y property
    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nice mtn")
font = pygame.font.Font(None, 38)

#load bitmap
clouds = pygame.image.load("L5_clouds.jpg").convert_alpha()
width_l, height_l = clouds.get_size()
# clouds = pygame.transform.scale(clouds, (width_l*2, height_l*2))
#load bitmap
heli = pygame.image.load("L5_Heli - Copy.png").convert_alpha()
width_p, height_p = heli.get_size()
heli = pygame.transform.scale(heli, (width_p//5, height_p//5))

mountain = pygame.image.load("L5_mountain - Copy.png").convert_alpha()
width, height = mountain.get_size()
mountain = pygame.transform.scale(mountain, (width//3, height//3))
#repeating loop



# white = 0,0,0


# textImage3 = font.render("MISSION IMPOSSIBLE", True, white)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.blit(clouds, (0, 0))
    screen.blit(heli, (500, 360))
    screen.blit(mountain, (300, 450))
    # screen.blit(textImage3, (300, 60))

    pygame.display.update()
