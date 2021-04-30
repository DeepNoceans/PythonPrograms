# Escape The Dragon Game

import sys
import time
import random
import math
import pygame
from pygame.locals import *

epic_gamer_score_exclusively_for_epic_gamers = 0

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)  # extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    #X property
    def _getx(self):
        return self.rect.x
    def _setx(self, value):
        self.rect.x = value
    X = property(_getx, _setx)

    #Y property
    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    Y = property(_gety, _sety)

    #position property
    def _getpos(self): return self.rect.topleft
    def _setpos(self, pos): self.rect.topleft = pos
    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
            "," + str(self.last_frame) + "," + str(self.frame_width) + \
            "," + str(self.frame_height) + "," + str(self.columns) + \
            "," + str(self.rect)


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def print_text2(font, x, y, text, color=(255, 50, 50)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def reset_arrow():
    y = random.randint(280, 350)
    arrow.position = 800, y

def reset_arrow2():
    y = random.randint(190, 230)
    arrow2.position = 800, y



#main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escape The Dragon Game")
font = pygame.font.Font(None, 18)
font2 = pygame.font.Font(None, 42)
font3 = pygame.font.Font(None, 42)


framerate = pygame.time.Clock()

#load bitmaps
bg = pygame.image.load("background.png").convert_alpha()

bill = pygame.image.load("flame.png").convert_alpha()
print(bill.get_size())

#create a sprite group
group = pygame.sprite.Group()

#create the dragon sprite
dragon = MySprite(screen)
dragon.load("dragon.png", 260, 150, 3)
dragon.position = 150, 230
group.add(dragon)

#create the player sprite
player = MySprite(screen)
player.load("caveman.png", 50, 64, 8)
player.first_frame = 1
player.last_frame = 7
player.position = 500, 303
group.add(player)

#create the arrow sprite
arrow = MySprite(screen)
arrow.load("Bill2.png", 26, 16, 1)
arrow.position = 1600, 320

arrow2 = MySprite(screen)
arrow2.load("Bill2.png", 26, 16, 1)
arrow2.position = 1600, 320

group.add(arrow)
group.add(arrow2)

arrow_vel = 8.0
arrow2_vel= 12
game_over = False
you_win = False
player_jumping = False
jump_vel = 0.0

jump_vel_boost = .08
player_start_y = player.Y
player_air = False
done = False
hit_test = False

#repeating loop
while not done:
    framerate.tick(95)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        done = True

    # Press SPACE?
    elif keys[K_SPACE]:
        if not player_jumping:
            player_jumping = True
            jump_vel = -6.0
            player_air = False

    # Holding SPACE?
    if keys[K_SPACE] and player_jumping and not player.Y <= 25:
            player_air = True

    # If holding space
    if player_air == True:
        jump_vel += jump_vel_boost
        player_air = False    
        jump_vel_boost += .005
        print("JumpING")
  
    # if let go (now ur falling)
    elif player.Y <= 25 or not keys[K_SPACE] and player_jumping:
        jump_vel += .5
        jump_vel_boost = .08
        print("let goooo")

    # if player.Y == player_start_y:
    #     player_jumping = False

    #update the arrow
    if not game_over:
        arrow.X -= arrow_vel
        arrow2.X -= arrow2_vel
        if arrow.X < -40:
            reset_arrow()
    #did arrow hit player?
    if pygame.sprite.collide_rect(arrow, player):
        reset_arrow()
        player.X -= 10
        dragon.X += 5

        hit_test = True

    if pygame.sprite.collide_rect(arrow2, player):
        reset_arrow2()
        player.X -= 10
        dragon.X += 5
        hit_test = True

    if arrow2.X <= 0:
        reset_arrow2()
    #did arrow hit dragon?
    if pygame.sprite.collide_rect(arrow, dragon):
        reset_arrow()
        dragon.X -= 10
        epic_gamer_score_exclusively_for_epic_gamers += 1

    if pygame.sprite.collide_rect(arrow2, dragon):
        reset_arrow2()
        dragon.X -= 10
        epic_gamer_score_exclusively_for_epic_gamers += 1

    #did dragon eat the player?
    if pygame.sprite.collide_rect(player, dragon):
        game_over = True

    #did the dragon get defeated?
    if dragon.X < -200:
        you_win = True
        game_over = True

    #is the player jumping?
    if player_jumping:
        player.Y += jump_vel
        # jump_vel += .05
        if player.Y > player_start_y:
            player_jumping = False
            player.Y = player_start_y
            jump_vel = 0.0

    #draw the background
    screen.blit(bg, (arrow.X, 0))
    screen.blit(bg, (arrow.X-799,0))
    screen.blit(bg, (arrow.X-1598, 0))
    



    #update sprites
    if not game_over:
        group.update(ticks, 50)

    #draw sprites
    group.draw(screen)

    print_text(font, 350, 560, "Press SPACE to jump!")
    print_text(font, 20, 50, f"Player X: {player.X}")
    print_text(font, 20, 65, f"Player Y: {player.Y}")
    
            
    if hit_test:
        print_text2(font3, 20, 20, f"Score: {epic_gamer_score_exclusively_for_epic_gamers}")

    else:
        print_text(
            font2, 20, 20, f"Score: {epic_gamer_score_exclusively_for_epic_gamers}")
    if arrow.X <= 400:
        hit_test = False        
        
    if game_over:
        print_text(font, 360, 100, "G A M E   O V E R")
        if you_win:
            print_text(font, 330, 130, "YOU BEAT THE DRAGON!")
        else:
            print_text(font, 330, 130, "THE DRAGON GOT YOU!")
    dragon.Y = player.Y - 70

    pygame.display.update()
