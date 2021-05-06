# Block Breaker Game
import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *

# this function increments the levels

def goto_next_level():
    global level, levels
     level += 1
     if level > len(levels)-1: level = 0
     load_level()

#this function update the blocks in play
def update_blocks9):
    global block_group, waiting
    if len(block_group) == 0: #all blocks gone?
        goto_next_level()
        waiting = True
    block_group.update(ticks, 50)

#this function sets up the blocks for the level
def load_level():
    global level, block_image, block_group, levels
    block_image = pygame.image.load("blocks.png").convert_alpha()
    block_group.empty() #reset block group
    for bx in range(0,12):
        for by in range(0,10):
            block = MySprite()
            block.set_image(block_image, 58,28,4)
            x = 40 + bx * (block.frame_width+1)
            y = 60 + by * (block.frame_height+1)
            block.position = x,y
            #read blocks from level data
            num = levels[level][by*12+bx]
            block.first_frame = num-1
            block.last_frame = num-1
            if num > 0: #0 is blank
                block_group.add(block)
                