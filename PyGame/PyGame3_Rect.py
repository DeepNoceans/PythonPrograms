import pygame

from pygame.locals import * 

pygame.init()


screen = pygame.display.set_mode((600,500))

pygame.display.set_caption("Drawing Rectangles")

pos_x = 200
pos_y = 250
vel_x = 2
vel_y = 1

while True: 
    for event in pygame.event.get(): 
        if event.type in (QUIT, KEYDOWN): 
            sys.exit()

if pos_x > 500 or pos_x < 0:
    vel_x = -vel_x

if pos_y > 400 or pos_y < 0:
    vel_y = -vel_y

screen.fill((0,0,200))

color = 255,255,0
pos = pos_x, pos_y, 100, 100
width = 0

pygame.draw.rect(screen, color, position, pos, width)

pygame.display.update()