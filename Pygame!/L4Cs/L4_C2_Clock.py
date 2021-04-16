import random, math, pygame
from datetime import datetime, date, time
from pygame.locals import *

#_analog Clock Demo


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText =  font.render(text, True, color)


    screen.blit(imgText, (x, y))


def print_text2(font, x, y, text, color=(40,80,160)):
    imgText = font.render(text, True, color)

    screen.blit(imgText, (x, y))


def wrap_angle(angle):
    return angle % 360

#main program begins pygame.init()

black = 0,0,0

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Analog Clock Demo")

font1 = pygame.font.Font(None, 66)

font2 = pygame.font.Font(None, 42)



minute_color = 120, 160, 255

white = 255, 255, 255


second_color = 130, 180, 255

hour_color = 200, 210, 255

pos_x = 300
pos_y = 250

radius = 250

angle = 360

done = False

#repeating loop

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:

        done = True

    screen.fill((50, 100, 200))

    #draw one step_around the circle
    pygame.draw.circle (screen, white, (pos_x, pos_y), radius, 6)

    #draw the clock numbers 1-12

    for n in range(1, 13):

        angle = math.radians(n * (360/12) - 90)
        x = math.cos(angle) * (radius-35) - 20
        y = math.sin(angle) * (radius-35) - 20

        print_text2(font1, pos_x+x, pos_y+y, str(n))

    

    #get the time of day
    
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    sec_angle = wrap_angle(seconds * (360/60) - 90)

    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius-40)
    sec_y = math.sin(sec_angle) * (radius-40)
    target = (pos_x+sec_x, pos_y+sec_y)
    target2 = (pos_x+sec_x-5, pos_y+sec_y-5)

    pygame.draw.line(screen, (40, 80, 160), (pos_x-5, pos_y-5), target2, 6)

    for n in range(1, 13):

        angle = math.radians(n * (360/12) - 90)
        x = math.cos(angle) * (radius-35) - 10
        y = math.sin(angle) * (radius-35) - 10

        print_text(font1, pos_x+x, pos_y+y, str(n))

    #draw the hours hand

    hour_angle = wrap_angle(hours * (360/12) - 90)
    hour_angle = math.radians(hour_angle)

    hour_x = math.cos(hour_angle) * (radius-80)

    hour_y=math.sin(hour_angle) * (radius-80)
    target=(pos_x+hour_x, pos_y+hour_y)

    pygame.draw.line(
        screen, hour_color, (pos_x-5, pos_y-5), target2, 17)

    # pygame.draw.line(
    #     screen, hour_color, (pos_x, pos_y), target, 17)


    #draw the minutes hand

    min_angle = wrap_angle(minutes * (360/60) - 90)
    min_angle = math.radians(min_angle)
    min_x = math.cos(min_angle) * (radius-60)
    min_y = math.sin(min_angle) * (radius-60)
    target = (pos_x+min_x, pos_y+min_y)
    target2 = (pos_x+min_x-5, pos_y+min_y-5)

    sec_angle = wrap_angle(seconds * (360/60) - 90)

    pygame.draw.line(screen, (40, 80, 160), (pos_x-5, pos_y-5), target2, 12)

    pygame.draw.line(screen, minute_color, (pos_x, pos_y), target, 12)

    #draw the seconds hand
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius-40)
    sec_y = math.sin(sec_angle) * (radius-40)
    target = (pos_x+sec_x, pos_y+sec_y)
    target2 = (pos_x+sec_x-5, pos_y+sec_y-5)

    pygame.draw.line(screen, second_color, (pos_x, pos_y), target, 6)

    minutes = "{:02d}".format(minutes)

    hours = "{:02d}".format(hours)

    seconds = "{:02d}".format(seconds)

    #cover the center
    pygame.draw.circle(screen, white, (pos_x, pos_y), 13)

    print_text2(font2, 245, 345, str(hours) + ":" +
               str(minutes) + ":" + str(seconds))
    print_text(font2, 250, 350, str(hours) + ":" + str(minutes) + ":" + str(seconds))

    pygame.display.update()



