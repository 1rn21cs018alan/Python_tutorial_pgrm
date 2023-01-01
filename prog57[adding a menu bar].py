#adding a menubar

from tkinter import *
from tkinter import Menu

window=Tk()
window.geometry("500x300")
window.title("Menu  Bar")


def click():
    print("clicked")


menu=Menu(window)
newItem=Menu(menu)
newItem.add_command(label="new",command=click)
newItem.add_separator()
newItem.add_command(label="Edit",command=click)

menu.add_cascade(label="File", menu=newItem)
window.config(menu=menu)




window.mainloop()
