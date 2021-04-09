import math, sys
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Pie Game - Presss 1,2,3,4")
myfont = pygame.font.Font(None, 60)


color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2

p1 = False
p2 = False
p3 = False
p4 = False


screenR = 0
screenG = 0
screenB = 100
RGBcycle = 3

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                p1 = True
            elif event.key == pygame.K_2:
                p2 = True
            
            elif event.key == pygame.K_3:
                p3 = True

            elif event.key == pygame.K_4:
                p4 = True

    screen.fill((screenR, screenG, screenB))

    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x+radius/2-20, y-radius/2))
    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x-radius/2, y-radius/2))
    textImg3 = myfont.render("3", True, color)
    screen.blit(textImg3, (x-radius/2, y+radius/2-20))
    textImg4 = myfont.render("4", True, color)
    screen.blit(textImg4, (x+radius/2-20, y+radius/2-20))

    if p1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color, (x, y), (x+radius, y), width)

    if p2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)

    if p3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x- radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y+radius), width)

    if p4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color, (x, y), (x-radius, y), width)

    if p1 and p2 and p3 and p4:
        color = 0,255,0

        if RGBcycle == 1:
            screenR += 1
            screenG -= 1
            screenB -= 1

        elif RGBcycle == 2:
            screenR -= 1
            screenG += 1
            screenB -= 1

        elif RGBcycle == 3:
            screenR -= 1
            screenG -= 1
            screenB += 1

        if screenR == 254 or screenG == 254 or screenB == 254:
            RGBcycle += 1
            if RGBcycle == 4:
                RGBcycle = 1

        if screenR <= 50:
            screenR += 1

        if screenG <= 50:
            screenG += 1

        if screenB <= 50:
            screenB += 1

    pygame.display.update()

    
