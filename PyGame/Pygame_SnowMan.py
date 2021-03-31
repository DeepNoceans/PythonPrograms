import pygame, math
from pygame.locals import * 

pygame.init()


screen = pygame.display.set_mode((600,500))

pygame.display.set_caption("Snowman")

while True: 
    for event in pygame.event.get(): 
        if event.type in (QUIT, KEYDOWN): 
            sys.exit()


    screen.fill((100,120,150))

    color = 255,255,255
    position =300,350
    radius= 100
    width = 0

    pygame.draw.circle(screen, color, position, radius, width)


    color = 255, 255, 255
    position = 300, 250
    radius = 75
    width = 0

    pygame.draw.circle(screen, color, position, radius, width)


    color = 255, 255, 255
    position = 300, 150
    radius = 50
    width = 0

    pygame.draw.circle(screen, color, position, radius, width)


    arcColor = 0,0,0
    arcPosition = 240,25,100,150
    start_angle = math.radians(250)
    end_angle = math.radians(295)
    arcWidth = 2

    pygame.draw.arc(screen, arcColor, arcPosition, start_angle, end_angle, arcWidth)



    eyeColor = 0,0,0
    eye1position = 280, 130
    eyeRadius = 5
    eyeWidth = 0

    pygame.draw.circle(screen, eyeColor, eye1position, eyeRadius, eyeWidth)

    eyeColor = 0, 0, 0
    eye2position = 310, 130
    eyeRadius = 5
    eyeWidth = 0

    pygame.draw.circle(screen, eyeColor, eye2position, eyeRadius, eyeWidth)


    stickcolor = 100, 70, 50

    stickwidth = 8

    pygame.draw.line(screen, stickcolor, (100, 250), (250, 225), stickwidth)

    stickcolor = 100, 70, 50

    stickwidth = 8

    pygame.draw.line(screen, stickcolor, (500, 250), (350, 225), stickwidth)

    pygame.display.update()
