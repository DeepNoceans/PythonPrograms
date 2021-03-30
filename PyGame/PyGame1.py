# http://www.pygame.org/docs/index.html

import pygame

from pygame.locals import * 

pygame.init()


white = 255,255,255 
blue = 0,0,200




screen = pygame.display.set_mode((600,500))

myfont = pygame.font.Font(None,60) 

textImage = myfont.render("Hello Pygame", True, white) 

screen.fill(blue) 
screen.blit(textImage, (100,100)) 
pygame.display.update()

while True: 
    for event in pygame.event.get(): 
        if event.type in (QUIT, KEYDOWN): 
            sys.exit()


    # screen.fill(blue) 
    # screen.blit(textImage, (100,100)) 
    # pygame.display.update()