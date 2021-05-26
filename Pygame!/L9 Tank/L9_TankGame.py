# Tank Battle Game
# Chapter 12

import sys
import time
import random
import math
import pygame
from pygame.locals import *
from MyLibrary3 import *


class Bullet():
    def __init__(self, position):
        self.alive = True
        self.color = (250, 20, 20)
        self.position = Point(position.x, position.y)
        self.velocity = Point(1, 1)
        self.rect = Rect(0, 0, 4, 4)
        self.owner = ""

    def update(self, ticks):
        self.position.x += self.velocity.x * 10.0
        self.position.y += self.velocity.y * 10.0
        if self.position.x < 0 or self.position.x > 800 \
                or self.position.y < 0 or self.position.y > 600:
            self.alive = False
        self.rect = Rect(self.position.x, self.position.y, 4, 4)

    def draw(self, surface):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, self.color, pos, 4, 0)


def fire_cannon(tank):
    position = Point(tank.turret.X, tank.turret.Y)
    bullet = Bullet(position)
    angle = tank.turret.rotation
    bullet.velocity = angular_velocity(angle)
    bullets.append(bullet)
    play_sound(shoot_sound)
    return bullet


def player_fire_cannon():
    bullet = fire_cannon(player)
    bullet.owner = "player"
    bullet.color = (30, 250, 30)


def enemy_fire_cannon():
    bullet = fire_cannon(enemy_tank)
    bullet.owner = "enemy"
    bullet.color = (250, 30, 30)


class Tank(MySprite):
    def __init__(self, tank_file="tank.png", turret_file="turret.png"):
        MySprite.__init__(self)
        self.load(tank_file, 50, 60, 4)
        self.speed = 0.0
        self.scratch = None
        self.float_pos = Point(0, 0)
        self.velocity = Point(0, 0)
        self.turret = MySprite()
        self.turret.load(turret_file, 32, 64, 4)
        self.fire_timer = 0

    def update(self, ticks):
        #update chassis
       
        MySprite.update(self, ticks, 100)
        self.rotation = wrap_angle(self.rotation)
        self.scratch = pygame.transform.rotate(self.image, -self.rotation)
        angle = wrap_angle(self.rotation-90)
        self.velocity = angular_velocity(angle)
        self.float_pos.x += self.velocity.x #* speed
        self.float_pos.y += self.velocity.y #* speed

        #warp tank around screen edges (keep it simple)
        if self.float_pos.x < -50:
            self.float_pos.x = 800
        elif self.float_pos.x > 800:
            self.float_pos.x = -50
        if self.float_pos.y < -60:
            self.float_pos.y = 600
        elif self.float_pos.y > 600:
            self.float_pos.y = -60

        #transfer float position to integer position for drawing
        self.X = int(self.float_pos.x)
        self.Y = int(self.float_pos.y)

        #update turret
        self.turret.position = (self.X, self.Y)
        self.turret.last_frame = 0
        self.turret.update(ticks, 100)
        self.turret.rotation = wrap_angle(self.turret.rotation)
        angle = self.turret.rotation+90
        self.turret.scratch = pygame.transform.rotate(
            self.turret.image, -angle)

   
    def draw(self, surface):
        #draw the chassis
        width, height = self.scratch.get_size()
        center = Point(width/2, height/2)
        surface.blit(self.scratch, (self.X-center.x, self.Y-center.y))
        #draw the turret
        width, height = self.turret.scratch.get_size()
        center = Point(width/2, height/2)
        surface.blit(self.turret.scratch, (self.turret.X-center.x,
                                           self.turret.Y-center.y))

    def __str__(self):
        return MySprite.__str__(self) + "," + str(self.velocity)


class EnemyTank(Tank):
    def __init__(self, tank_file="enemy_tank.png", turret_file="enemy_turret.png"):
        Tank.__init__(self, tank_file, turret_file)

    def update(self, ticks):
        
        Tank.update(self, ticks)

    def draw(self, surface):
        Tank.draw(self, surface)


#this function initializes the game
def game_init():
    global screen, backbuffer, font, timer, player_group, player, \
        enemy_tank, bullets, crosshair, crosshair_group

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    backbuffer = pygame.Surface((800, 600))
    pygame.display.set_caption("Tank Battle Game")
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    #load mouse cursor
    crosshair = MySprite()
    crosshair.load("crosshair.png")
    crosshair_group = pygame.sprite.GroupSingle()
    crosshair_group.add(crosshair)

    #create player tank
    player = Tank()
    player.float_pos = Point(400, 300)
    
    #create enemy tanks
    enemy_tank = EnemyTank()
    enemy_tank.float_pos = Point(random.randint(50, 760), 50)
    enemy_tank.float_pos = Point(410, 300)
    enemy_tank.rotation = 135
    
    #create bullets
    bullets = list()

# this function initializes the audio system


def audio_init():
    global shoot_sound, boom_sound

    #initialize the audio mixer
    pygame.mixer.init()

    #load sound files
    shoot_sound = pygame.mixer.Sound("shoot.wav")
    boom_sound = pygame.mixer.Sound("boom.wav")


# this function uses any available channel to play a sound clip
def play_sound(sound):
    channel = pygame.mixer.find_channel(True)
    channel.set_volume(0.5)
    channel.play(sound)


#main program begins
game_init()
audio_init()
game_over = False
player_score = 0
enemy_score = 0
last_time = 0
mouse_x = mouse_y = 0
player_dead = False
enemy_dead = False
rotation_goal = 135
USEREVENT = 0

testf = USEREVENT + 1

pygame.time.set_timer(testf, 500)

player_health = 10
enemy_health = 5

#main loop
while True:
    keys = pygame.key.get_pressed()
    timer.tick(80)
    ticks = pygame.time.get_ticks()

    #reset mouse state variables
    mouse_up = mouse_down = 0
    mouse_up_x = mouse_up_y = 0
    mouse_down_x = mouse_down_y = 0

    # rotation_goal = pygame.math.Vector2().angle_to(
    #     player.float_pos - player.float_pos)


    # ui








    #event section
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            move_x, move_y = event.rel
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            mouse_down_x, mouse_down_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouse_up = event.button
            mouse_up_x, mouse_up_y = event.pos
        # if event.type == testf:
        #     print(rotation_goal)


        
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_e]:
        player.float_pos = Point(stayX, stayY)
    if keys[K_1]:
        player.X = 50
        player.Y = 50

    elif keys[K_2]:
        player.X = 750
        player.Y = 50

    elif keys[K_3]:
        player.X = 50
        player.Y = 550

    elif keys[K_4]:
        player.X = 750
        player.Y = 550

            
        # if event.type == testf:
        #     rotation_goal = random.randint(1, 360)
    if rotation_goal != enemy_tank.rotation:
        if rotation_goal < enemy_tank.rotation:
            enemy_tank.rotation -= 3
        elif rotation_goal > enemy_tank.rotation:
            enemy_tank.rotation += 3

    #get key states
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    elif keys[K_LEFT] or keys[K_a] or keys[K_s]:
        #calculate new direction velocity
        player.rotation -= 2.0

    elif keys[K_RIGHT] or keys[K_d] or keys[K_f]:
        #calculate new direction velocity
        player.rotation += 2.0

    #fire cannon!
    if keys[K_SPACE] or mouse_up > 0:
        if ticks > player.fire_timer + 1000:
            player.fire_timer = ticks
            player_fire_cannon()

    #update section
    if not game_over:
        crosshair.position = (mouse_x, mouse_y)
        crosshair_group.update(ticks)

        #point tank turret toward crosshair
        angle = target_angle(player.turret.X, player.turret.Y,
                             crosshair.X + crosshair.frame_width/2,
                             crosshair.Y + crosshair.frame_height/2)
        angle = (angle + 360) % 360


        player.turret.rotation = angle

        angle = target_angle(enemy_tank.turret.X, enemy_tank.turret.Y,
                                player.X + crosshair.frame_width/2,
                                player.Y + crosshair.frame_height/2)
        angle = (angle + 360) % 360

        
        enemy_tank.turret.rotation = angle

        angle = (angle + 360) % 360

        
        
        if enemy_tank.turret.rotation > rotation_goal:
            rotation_goal += 4
        if enemy_tank.turret.rotation < rotation_goal:
            rotation_goal -= 4
        #move tank
        player.update(ticks)

        #update enemies
        enemy_tank.update(ticks)
        if ticks > enemy_tank.fire_timer + 1000:
            enemy_tank.fire_timer = ticks
            enemy_fire_cannon()

        #update bullets
        for bullet in bullets:
            bullet.update(ticks)
            if bullet.owner == "player":
                if pygame.sprite.collide_rect(bullet, enemy_tank):
                    player_score += 1
                    enemy_health -= 1
                    bullet.alive = False
                    play_sound(boom_sound)
            elif bullet.owner == "enemy":
                if pygame.sprite.collide_rect(bullet, player):
                    enemy_score += 1
                    player_health -= 1
                    bullet.alive = False
                    play_sound(boom_sound)

    if player_health == 0:
        player_health = 10
        player.float_pos = Point(410,300)
    

    if enemy_health == 0:
        enemy_health = 5
        enemy_tank.float_pos = Point(410, 300)


    # if player.X == 0:
    #     player.X = 1
    # if player.Y == 0:
    #     player.Y = 1
    # if enemy_tank.X == 0:
    #    enemy_tank.X = 1 
    # if enemy_tank.Y == 0:
    #     enemy_tank.Y = 1
    # angleA_X, angleA_Y = player.X, player.Y
    # angleB_X, angleB_Y = enemy_tank.X, enemy_tank.Y


    # deltaX = angleB_X - angleA_X
    # deltaY = angleB_Y - angleA_Y
    # if deltaX == 0:
    #     deltaX = 1
    # if deltaY == 0:
    #     deltaY = 1
    # # print(deltaX, "                     ", deltaY)
    # tan = deltaX/deltaY


    # formula = math.atan(tan)

    # formula = formula ** 2
    # formula = math.sqrt(formula)

    # # formula = math.degrees(formula)

    # if player.X <= enemy_tank.X and player.Y < enemy_tank.Y:
    #     formula += 270
    #     print("E E E E E e E E E EE  E E EE E E E E E EE E E E ")

    # #Good
    # elif player.X <= enemy_tank.X and player.Y > enemy_tank.Y:
    #     formula += 180
    #     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH")


    # elif player.X >= enemy_tank.X and player.Y > enemy_tank.Y:
    #     formula += 90
    #     print("1234 1234 1234 1234123 41234 123 123 ")

    # rotation_goal = formula

    # print(rotation_goal)

    # enemy_tank.float_pos = Point(410, 300)
    #drawing section
    backbuffer.fill((100, 100, 20))

    for bullet in bullets:
        bullet.draw(backbuffer)

    enemy_tank.draw(backbuffer)

    player.draw(backbuffer)

    crosshair_group.draw(backbuffer)

    screen.blit(backbuffer, (0, 0))

    if rotation_goal == 360:
        rotation_goal = 0
        enemy_tank.rotation = 0

    pygame.draw.rect(screen, (50, 150, 50, 180), Rect(10, 570, player_health*20, 25))
    pygame.draw.rect(screen, (100, 200, 100, 180), Rect(10, 570, 200, 25), 2)

    pygame.draw.rect(screen, (50, 150, 50, 180), Rect(590, 570, enemy_health*40, 25))
    pygame.draw.rect(screen, (100, 200, 100, 180), Rect(590, 570, 200, 25), 2)

    if not game_over:
        print_text(font, 200, 0, "PLAYER " + str(player_score))
        print_text(font, 500, 0, "ENEMY " + str(enemy_score))
        print_text(font, 350, 20, "Goal: " + str(rotation_goal))
        print_text(font, 350, 40, "Angle: " + str(enemy_tank.rotation))
    else:
        print_text(font, 0, 0, "GAME OVER")

    stayX = player.X
    stayY = player.Y
    pygame.display.update()

    #remove expired bullets
    for bullet in bullets:
        if bullet.alive == False:
            bullets.remove(bullet)
