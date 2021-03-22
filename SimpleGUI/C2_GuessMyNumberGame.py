from tkinter import *

class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
        text = "Welcome to the Guess My Number Game"
        ).grid(row = 0)

        Label(self,
              text="Guess from 0-1000: "
              ).grid(row=1, column=0)
        self.guessed_num = Entry(self)
        self.guessed_num.grid(row=1, column=1, sticky=W)

        Button(self,
               text="Check your guess",
               command=self.tell_story
               ).grid(row=3, column=0, sticky=W)
            self.story_txt = Text(self, width=20, height=10, wrap=WORD)
            self.story_txt.grid(row=7, column=0, columnspan=4)
# main
root = Tk()
root.title("Mad Lib")
root.geometry("300x150")
app = Application(root)
root.mainloop()
