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

def game_init():
    global screen, font, timer
    global paddle_group, block_group, ball_group
    global paddle, block_image, block, ball_group

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Block Breaker Game")
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()

    #create sprite gorups
    paddle_group = pygame.sprite.Group()
    blocks group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()
    
    #create the paddle sprite
    paddle = MySprite()
    paddle.load("paddle.png")
    paddle.position = 400,540
    paddle_group.add(paddle)

    #create ball sprite
    ball = MySprite()
    ball.load("ball.png")
    ball.position = 400, 300
    ball_group.add(ball)

def move_paddle():
    global movex, movey, keys, waiting
    paddle_group.update(ticks, 50)
    if keys[K_SPACE]:
        if waiting:
            waiting = False
            reset_ball()
    elif keys[K_LEFT]:
        paddle.velocity.X = -10.0
    elif keys[K_RIGHT]:
        paddle.velocity.X = 10.0
    else:
        if movex < -2:
            paddle.velocity.x = movex
        elif movex > 2:
            paddle.velocity.x = movex
        else:
            paddle.velocity.x = 0

    paddle.X += paddle.velocity.x
    if paddleX < 0:
        paddle.X = 0
    elif paddle.X > 710:
        paddle.X = 710

def reset_ball():
    ball.velocity = Point(4.5, - 7.0)


# this function moves the ball
def move_ball():
    global waiting, ball, game_over, liv
    #move the ball
    ball_group.update(ticks, 50)
    if waiting:
        ball.X = paddle.X + 40
        ball.Y = paddle.Y - 20
        ball.X < 0:
        ball.X = 0:



                