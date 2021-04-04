import pygame, math, sys
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


    nosecolor = 255, 140, 0
    nosepos = [(295, 145), (275, 155),(300, 155)]

    pygame.draw.polygon(screen, nosecolor, nosepos, width = 0)

    E1rect = 250,95, 100, 20 
    pygame.draw.ellipse(screen, eyeColor, E1rect, width = 0)




    arcColor = 0,0,0
    arcPosition = 240,25,100,150
    start_angle = math.radians(250)
    end_angle = math.radians(295)
    arcWidth = 2

    pygame.draw.arc(screen, arcColor, arcPosition, start_angle, end_angle, arcWidth)


    arc2Position = 275, 50, 50, 10
    start_angle2 = math.radians(0)
    end_angle2 = math.radians(180)
    pygame.draw.arc(screen, arcColor, arc2Position, start_angle2, end_angle2, width=50050)

    Rect1color = 0, 0, 0
    Rect1pos = 275, 55, 50, 50
    Rect1width = 0

    pygame.draw.rect(screen, Rect1color, Rect1pos, Rect1width)
    


    pygame.draw.circle(screen, (255,200,0), (550,20), 50, width = 0)

    pygame.display.update()


   
