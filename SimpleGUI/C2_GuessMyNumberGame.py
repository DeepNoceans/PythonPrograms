from tkinter import *

import random

rand_num = random.randint(1, 999)


class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Welcome to the Guess My Number Game"
        ).grid(row = 0)

        Label(self,
              text="\nGuess from 1-1000:"
                            ).grid(row=1, column=0)
        self.guessed_num = Entry(self)
        self.guessed_num.grid(row=2, column=0)

        Button(self,
               text="Check your guess",
               command=self.result
               ).grid(row=4, column=0)
        self.result_txt = Text(self, width=15, height=2, wrap=WORD)
        self.result_txt.grid(row=5, column=0)

    def result(self):
        g_num = self.guessed_num.get()

        if int(g_num) == rand_num:
            result = "Correct."
        else:
            result = "Incorrect."
            if int(g_num) > rand_num:
                result += " Guess smaller."
            elif int(g_num) < rand_num:
                result += " Guess larger."
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, result)


            
# main
root = Tk()
root.title("Mad Lib")

app = Application(root)


root.mainloop()
