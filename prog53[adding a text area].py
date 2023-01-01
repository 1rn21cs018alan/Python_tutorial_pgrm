#adding a text area
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
window=Tk()
window.title("Text area")
window.geometry("720x480")

text1=scrolledtext.ScrolledText(window, width=40,height=10)
text1.grid(column=0,row=0)
text1.insert(INSERT,"Your text goes here")


def click():
    text1.delete(1.0,END)

button1=Button(window,text="clear text",command=click)
button1.grid(column=0,row=1)

window.mainloop()
