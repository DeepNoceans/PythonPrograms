from tkinter import *

import random

rand_num = random.randint(1, 999)

class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        # self.num_attempts = 0

    def create_widgets(self):
        Label(self,
              text="Welcome to the Guess My Number Game",
              font=("Times New Roman", 12,"bold")
              ).grid(row = 0)

        Label(self,
              text="\nGuess from 1-1000:"
              ).grid(row=1, column=0)
        self.guessed_num = Entry(self)
        self.guessed_num.grid(row=2, column=0)

        Button(self,
               text="Check your guess",
               bg="black",
               fg="white",
               command=self.result,
               ).grid(row=4, column=0)


        self.is_correct= Label(self,
              text="Take a guess...",
              font=("Arial", 10,),
              bg="#ffffff"
              ).grid(row=5,column=0)

    def result(self):
        guessed_num = self.guessed_num.get()

        # if self.num_attempts != 0:
        #     self.num_attempts = 0

        if guessed_num.isdigit():
            print(3334443)
            # self.num_attempts += 1
            int_guessed = int(self.guessed_num.get())

            print(int_guessed)

            if int_guessed == rand_num:
                self.is_correct.config(text = "Correct.")
                # result += " It took you " + str(self.num_attempts) + " attempts."
                self.is_correct.config(bg = "#7cff48")

            else:
                self.is_correct.configure(bg = "#ff4848")

            if int_guessed > rand_num:
                self.is_correct["text"] = "Guess smaller."
                # result += " Attempt: " + str(self.num_attempts)
                self.is_correct.config(text="Guess smaller.")

            elif int_guessed < rand_num:
                self.is_correct.config(text="Guess larger.")
                # result += " Attempt: " + str(self.num_attempts)
                print(1)
                #self.is_correct.config(text="Guess larger.")



        else:
            result = "Not digit."



            
# main
root = Tk()
root.title("GuessMyNumberGame")

app = Application(root)


root.mainloop()
