import pygame
import random
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Crazy Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((100, 120, 150))


    for i in range(0, 1000):

        # screen.fill((100, 120, 150))


        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
        
        start_position = random.randint(0, 1000), random.randint(0, 1000)
        
        end_position = random.randint(0, 1000), random.randint(0, 1000)

        width = 1
        pygame.draw.line(screen, color, start_position, end_position, width)

    pygame.display.update()
