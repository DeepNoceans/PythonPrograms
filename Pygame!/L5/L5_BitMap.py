import sys, random, math, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def wrap_angle(angle):
    return angle % 360

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
font = pygame.font.Font(None, 18)


#load bitmap
space = pygame.image.load("space.png").convert_alpha()

#load bitmap
planet = pygame.image.load("planet2.png").convert_alpha()
width, height = planet.get_size()

ship = pygame.image.load("freelance.png").convert_alpha()
ship = pygame.transform.scale(ship, (width//2, height//2))
#repeating loop

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

radius = 250
angle = 0.0
pos = Point(0,0)
old_pos = Point(0,0)


angle = wrap_angle(angle - 0.1)
pos.x = math.sin(math.radians(angle)) * radius
pos.y = math.cos(math.radians(angle)) * radius

width, height = ship.get_size()
screen.blit(ship, (400 + pos.x-width // 2, 300 + pos.y-height // 2))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    
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
    screen.blit(space, (0,0))

    screen.blit(planet, (350-width/2,250-height/2))

    width, height = scratch_ship.get_size()
    x = 400+pos.x-width//2
    y = 300+pos.y-height//2
    
    screen.blit(scratch_ship, (x,y))

    pygame.display.update()
