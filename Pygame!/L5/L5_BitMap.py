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


def wrap_angle(angle):
    return angle % 360


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
font = pygame.font.Font(None, 38)


#load bitmap
space = pygame.image.load("space.png").convert_alpha()

#load bitmap
planet = pygame.image.load("planet2.png").convert_alpha()
width_p, height_p = planet.get_size()

ship = pygame.image.load("freelance.png").convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.scale(ship, (width//3, height//3))
#repeating loop


radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)
pos.x = math.sin(math.radians(angle)) * radius
pos.y = math.cos(math.radians(angle)) * radius

cir = math.pi * radius * 2
cir = "{:.002f}".format(cir)
vel = .01

white = 255, 255, 255
# myfont = pygame.font.Font(None, 20)
textImage = font.render(f"Orbiral Circumference: {cir}", True, white)

width, height = ship.get_size()
screen.blit(ship, (400 + pos.x-width // 2, 300 + pos.y-height // 2))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_EQUALS]:
        vel += .001
    if keys[K_MINUS]:
        vel -= .001
        if vel <= 0:
            vel = 0

    angle = wrap_angle(angle - vel)

    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    rangle = math.atan2(delta_y, delta_x)
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)

    old_pos.x = pos.x
    old_pos.y = pos.y

    angle = wrap_angle(angle - 0.1)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius

    #draw background
    screen.blit(space, (0, 0))

    screen.blit(textImage, (0, 0))

    screen.blit(planet, (400-width_p/2, 300-height_p/2))

    width, height = scratch_ship.get_size()
    x = 400+pos.x-width//2
    y = 300+pos.y-height//2

    screen.blit(scratch_ship, (x, y))

    pygame.display.update()
