#label font size and window size

from tkinter import *

window= Tk()
window.title("My third GUI")
label1=Label(window, text="MOOOOO says multiple Cows",font= ("Arial Bold" ,50)) #says what it is.
label1.grid(column=0,row=0)
window.geometry("1500x850")# this is the window scale in pixels


window.mainloop()
