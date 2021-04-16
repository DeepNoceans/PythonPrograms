
import sys, random, math, pygame
from pygame.locals import *

#main program begins

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Circle Demo")
screen.fill((0,0,100))

pos_x = 300

pos_y = 250

radius = 200

angle = 360

wide = 40

wide_change = -1

#repeating loop while True:
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()


    #increment angle

    angle += 1

    if angle >= 360:

        angle = 0

        r = random.randint(0,255)

        g = random.randint(0,255)

        b = random.randint(0,255)

        color = r,g,b


        wide += wide_change
        if wide == 40:
           wide_change = -1
        
        elif wide == 1:
           wide_change = 1



    #calculate coordinates

    x = math.cos( math.radians (angle)) * radius
    y = math.sin( math.radians (angle)) * radius

    #draw one step around the circle
    pos = (int(pos_x + x), int(pos_y + y)), (int(pos_x + x)+20,
                                             int(pos_y + y)+20), (int(pos_x + x)-40, int(pos_y + y)-40), (int(pos_x + x)+100, int(pos_y + y)-10)

    pygame.draw.polygon(screen,color,pos, 0)
    # pygame.draw.circle(screen, color, pos, wide, 0)

    pygame.display.update()
