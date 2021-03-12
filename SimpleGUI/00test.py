from tkinter import *

root = Tk()
root.title("Go!")
root.geometry("200x100")


#create a frame (holds other widgets, in window)
app = Frame(root)
app.grid()

#create button (in frame)
button1 = Button(app, text = "Go!")
button1.grid()
button1.configure(text = "Warning")
root.mainloop()
