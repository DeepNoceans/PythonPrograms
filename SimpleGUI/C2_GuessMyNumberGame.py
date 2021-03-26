from tkinter import *

import random

rand_num = random.randint(1, 999)

class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self["bg"] = 
        # self.num_attempts = 0

    def create_widgets(self):
        Label(self,
              text="Welcome to the Guess My Number Game",
              font=("Times New Roman", 12)
              ).grid(row = 0)

        Label(self,
              text="\nGuess from 1-1000:"
              ).grid(row=1, column=0)
        self.guessed_num = Entry(self)
        self.guessed_num.grid(row=2, column=0)

        Button(self,
               text="Check your guess",
               command=self.result,
               bg="black",
               fg="white"
               ).grid(row=4, column=0)


        Label(self,
              text="Take a guess...",
              font=("Arial", 10),
              variable=result
              ).grid(row=5,column=0)

    def result(self):
        g_num = self.guessed_num.get()

        # if self.num_attempts != 0:
        #     self.num_attempts = 0

        if g_num.isdigit():

            # self.num_attempts += 1

            if int(g_num) == rand_num:
                self.result["text"] = "Correct."
                # result += " It took you " + str(self.num_attempts) + " attempts."
                self.result["bg"] = "#7CFF48"
            else:
                self.result["bg"] = "#FF4848"

                if int(g_num) > rand_num:
                    self.result["text"] = "Guess smaller."
                    # result += " Attempt: " + str(self.num_attempts)

                elif int(g_num) < rand_num:
                    self.result["text"] = "Guess larger."
                    # result += " Attempt: " + str(self.num_attempts)
        else:
            result = "Not digit."

        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, result)


            
# main
root = Tk()
root.title("GuessMyNumberGame")

app = Application(root)


root.mainloop()
