# Mohamad Moussaoui
#4/6/2021


import pygame
import sys
from pygame.locals import *



# myfont = pygame.font.Font("Arial", 30) 

# fonts = pygame.font.get_fonts() 
# print(len(fonts)) 
# for f in fonts:
#     print(f)

# image = font.render(text, True, (255, 255, 255))
# screen.blit(image, (100, 100))



class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct= 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        #read trivia data from file
        f = open(filename, "r")
        trivia_data = f.readlines()
        f.close()

        #count and clean up trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

    def show_question(self):
        print_text(font1, 210, 5, "Trivia Game")
        print_text(font2, 190, 500-20, "Press Keys (1-4) To Answer", purple)
        print_text(font2, 530, 5, "Score", purple)
        print_text(font2, 550, 25, str(self.score), purple)

        #get correct answer out of date (first)
        self.correct = int(self.data[self.current+5])

        #display question
        question = self.current // 6 + 1
        print_text(font1, 5, 80, "Question " + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        #respond to correct answer
        if self.scored:
            self.colors = [white, white, white, white]
            self.color[self.correct-1] = green
            print_text(font1, 230, 380, "Correct!", green)
            print_text(font2, 170, 420, "Press Enter For Next Question", green)

        elif self.failed:
            self.colors = [white, white, white, white]
            self.color[self.correct-1] = red
            print_text(font1, 220, 380, "Incorrect!", red)
            print_text(font2, 170, 420, "Press Enter For Next Question", red)

        #display answers
        print_text(font1, 5, 170, "ANSWERS")

        print_text(font2, 20, 210, "1 - " + self.data[self.current+1], self.colors[0])

        print_text(font2, 20, 240, "2 - " + self.data[self.current+2], self.colors[1])

        print_text(font2, 20, 270, "3 - " + self.data[self.current+3], self.colors[2])

        print_text(font2, 20, 300, "4 - " + self.data[self.current+4], self.colors[3])

    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white,white,white,white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0

    def print_text(font, x, y, text, color = (255,255,255), shadow = True):
        if shadow:
            imgText = font.render(text, True, (0,0,0))
            screen.blit(imgText, (x-2, y-2))
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x,y))

#main program begins
pygame.init()
screen = pygame. display.set_made((600, 500))
pygame.display.set_caption("The Truvia Game")
fon1 = pygame.font.Font(None, 40)
font2 = pygame.dont.Font(None, 24)
white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0

#load the trivia data file
trivia = Trivia("Trivia_Data.text")

#repeating loop 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit
        elif event.key == pygame.K_1:
            trivia.handle_input(1)
        elif event.key == pygame.K_2:
            trivia.handle_input(2)
        elif event.key == pygame.K_3:
            trivia.handle_input(3)
        elif event.key == pygame.K_4:
            trivia.handle_input(4)
        elif event.key == pygame.K_RETURN:
            trivia.next_question()

#clear the screen
screen.fill((100,100,200))

#display trivia data
trivia.show_question()

#update the display
pygame.display.update()
