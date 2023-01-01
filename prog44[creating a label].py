#creating a label

from tkinter import *
window=Tk()
window.title=("Our Second GUI")

label1=Label(window, text="Moo says the Cow")
label1.grid(column=0, row=0)

window.mainloop()
