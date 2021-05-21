# Block Breaker Game
import sys
import time
import random
import math
import pygame
from pygame.locals import *
from MyLibrary import *
levels = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                                 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2,
                                                 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2,
                                                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                                 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2,
                                                 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2,
                                                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                                                                       3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3,
                                                                                       3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3,
                                                                                       3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3,
                                                                                       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                                                                       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                                                                       3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3,
                                                                                       3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3,
                                                                                       3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3,
                                                                                       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


# this function increments the levels
def goto_next_level():
    global level, levels
    level += 1
    if level > len(levels)-1:
        level = 0
    load_level()


#this function update the blocks in play
def update_blocks():
    global block_group, waiting
    if len(block_group) == 0:  # all blocks gone?
        goto_next_level()
        waiting = True
    block_group.update(ticks, 50)


#this function sets up the blocks for the level
def load_level():
    global level, levels, block_image, block_group
    block_image = pygame.image.load("blocks.png").convert_alpha()

    #Challenge 2
    # block2_image = pygame.image.load("blocks2.png").convert_alpha()

    block_group.empty()  # reset block group
    for bx in range(0, 12):
        for by in range(0, 12):
            block = MySprite()
            block.set_image(block_image, 58, 28, 4)
            x = 40 + bx * (block.frame_width+1)
            y = 60 + by * (block.frame_height+1)
            block.position = x, y

            #read blocks from level data
            num = levels[level][by*12+bx]
            block.first_frame = num-1
            block.last_frame = num-1
            if num > 0:  # 0 is blank
                block_group.add(block)


# def game_init():
global screen, font, timer
global paddle_group, block_group, ball_group
global paddle, block_image, block, ball_group

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Block Breaker Game")
font = pygame.font.Font(None, 36)
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

timer = pygame.time.Clock()

#create sprite gorups
paddle_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

#create the paddle sprite
paddle = MySprite()
paddle.load("paddle.png")
paddle.position = 400, 540
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
            print("movex < -2")
        elif movex > 2:
            paddle.velocity.x = movex
            print("movex > 2")

        else:
            paddle.velocity.x = 0

    paddle.X += paddle.velocity.x
    if paddle.X < 0:
        paddle.X = 0
    elif paddle.X > 710:
        paddle.X = 710


def reset_ball():
    # ball.velocity = Point(4.5, - 7.0)

    # Challenge 3
    vel_x = random.randint(2, 10)
    vel_y = random.randint(-14, -3)
    ball.velocity = Point(vel_x, vel_y)


# this function moves the ball
def move_ball():
    global waiting, ball, game_over, lives
    #move the ball
    ball_group.update(ticks, 50)
    if waiting:
        ball.X = paddle.X + 37
        ball.Y = paddle.Y - 10

        # Challenge 3
        # vel_x = random.randint(2, 20)
        # vel_y = random.randint(-14, -3)
        # ball.velocity = Point(vel_x, vel_y)

    ball.X += ball.velocity.x
    ball.Y += ball.velocity.y
    if ball.X < 0:
        ball.X = 0
        ball.velocity.x *= -1
    elif ball.X > 780:
        ball.X = 780
        ball.velocity.x *= -1
    if ball.Y < 0:
        ball.Y = 0
        ball.velocity.y *= -1
    elif ball.Y > 580:  # missed paddle
        waiting = True
        lives -= 1
        if lives < 1:
            game_over = True


# this function test for collision between ball and paddle
def collision_ball_paddle():
    if pygame.sprite.collide_rect(ball, paddle):

        vel_x = random.randint(1, 8)
        vel_y = random.randint(-8, -1)
        ball.velocity = Point(vel_x, vel_y)

        # abs() is absolute value of number in ()
        ball.velocity.y = -abs(ball.velocity.y)
        bx = ball.X + 8
        by = ball.Y + 8
        px = paddle.X + paddle.frame_width/2
        py = paddle.Y + paddle.frame_height/2
        if bx < px:  # left side of paddle?
            ball.velocity.x = -abs(ball.velocity.x)
        else:  # right side of paddle?
            ball.velocity.x = abs(ball.velocity.x)


def collision_ball_blocks():
    global score, block_group, ball
    hit_block = pygame.sprite.spritecollideany(ball, block_group)
    if hit_block != None:
        score += 10
        block_group.remove(hit_block)
        bx = ball.X + 8
        by = ball.Y + 8

        #hit middle of block from above or below?
        if bx > hit_block.X+5 and bx < hit_block.X + hit_block.frame_width-5:
            if by < hit_block.Y + hit_block.frame_height/2:  # above?
                ball.velocity.y = -abs(ball.velocity.y)
            else:  # belo2w?
                ball.velocity.y = abs(ball.velocity.y)

        # hit left side of block?
        elif bx < hit_block.X + 5:

            ball.velocity.x = -abs(ball.velocity.x)

        # hit right side of block?
        elif bx > hit_block.X + hit_block.frame_width - 5:
            ball.velocity.x = abs(ball.velocity.x)

        #handle any other situation
        else:
            ball.velocity.y *= -1


# MAIN CODE
# game_init()
game_over = False
waiting = True
score = 0
lives = 3
level = 0
load_level()

movex, movey = 0, 0




while True:
    timer.tick(60)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        elif event.type == MOUSEMOTION:
            print(str(event.rel))
            movex, movey = event.rel

        elif event.type == MOUSEBUTTONUP:
            if waiting:
                waiting = False
                reset_ball()

        elif event.type == KEYUP:
            if event.key == K_RETURN:
                goto_next_level()

    #handle key presses
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    #do updates
    if not game_over:
        update_blocks()
        move_paddle()
        move_ball()
        collision_ball_paddle()
        collision_ball_blocks()

    #drawing
    screen.fill((60, 180, 180))

    block_group.draw(screen)
    ball_group.draw(screen)
    paddle_group.draw(screen)
    print_text(font, 0, 0, "SCORE " + str(score))
    print_text(font, 200, 0, "LEVEL " + str(level + 1))
    print_text(font, 400, 0, "BLOCKS " + str(len(block_group)))
    print_text(font, 670, 0, "BALLS " + str(lives))
    if game_over:
        print_text(font, 270, 440, "G A M E  O V E R")

    pygame.display.update()
