import sys, random, math, pygame
from pygame.locals import *

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")



#load bitmap
space = pygame.image.load("space.png").convert_alpha()

#load bitmap
space = pygame.image.load("space.png").convert_alpha()
planet = pygame.image.load("planet2.png").convert_alpha()
width, height = planet.get_size()

ship = pygame.image.load("freelance.png").convert_alpha()
ship = pygame.transform.scale(ship, (width//2, height//2))
#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    
    #draw background
    screen.blit(space, (0,0))

    screen.blit(planet, (400-width/2,300-height/2))


    screen.blit(ship, (20,50))

    pygame.display.update()
