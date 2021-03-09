#Lazy Buttons 
#Demonstrates creating buttons

from tkinter import *

# create a root window
root = Tk()
root.title("Lazy buttons")
root.geometry("200x100")

#create a fram in the window to hold other widgets
app = Frame (root)
app.grid()

# create a button in the frame
bttnl = Button(app, text = "I do nothing!")
bttnl.grid()

# create a second button in the fframe
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me too!")

#create a thrid button in th ferame
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "same here!"

# kick off the root window's event log

root.mainloop()