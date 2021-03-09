from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """
    def __init__(self, master):
        """Initialize the Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create three buttons that do nothing."""

        # create a button in the frame
        bttnl = Button(self, text="I do nothing!")
        bttnl.grid()

        # create a second button in the fframe
        bttn2 = Button(self)
        bttn2.grid()
        bttn2.configure(text="Me too!")

        #create a thrid button in th ferame
        bttn3 = Button(self)
        bttn3.grid()
        bttn3["text"] = "same here!"


# main
root = Tk()
root.title("Lazy buttons")
root.geometry("200x100")
app = Application(root)
root.mainloop()