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
pygame.display.set_caption("Nice Lake")
font = pygame.font.Font(None, 38)


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

#load bitmap
lake = pygame.image.load("L5_Lake2.jpg").convert_alpha()
width_l, height_l = lake.get_size()
lake = pygame.transform.scale(lake, (width_l*2, height_l*2))
#load bitmap
dolphin = pygame.image.load("L5_Dolphin.png").convert_alpha()
width_p, height_p = dolphin.get_size()
dolphin = pygame.transform.scale(dolphin, (width_p//5, height_p//5))

boat = pygame.image.load("L5_Boat.png").convert_alpha()
width, height = boat.get_size()
boat = pygame.transform.scale(boat, (width//3, height//3))
#repeating loop


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()



    screen.blit(lake, (0, 0))
    screen.blit(dolphin, (500, 500))
    screen.blit(boat, (150, 500))
    pygame.display.update()


