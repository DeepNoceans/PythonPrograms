import pygame

from pygame.locals import *
pygame.init()

# how to use pygame.time.set_timer(event, milliseconds)

USEREVENT = 0

testf = USEREVENT + 1

pygame.time.set_timer(testf, 1000)




while True:
    for event in pygame.event.get():
        if event.type == testf:
            print("TEST")




