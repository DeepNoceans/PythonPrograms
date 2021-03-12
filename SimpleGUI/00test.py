from tkinter import *

root = Tk()
root.title("Go!")
root.geometry("500x500")
root.mainloop()

#create a frame (holds other widgets, in window)
app = Frame (root)
app.grid()

#create button (in frame)
button1 = Button(app)
button1.grid()
