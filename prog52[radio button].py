#radio button

from tkinter import *
from tkinter.ttk import *

window=Tk ()
window.title ("Radio button")
window.geometry ("500x600")

def click1():
    label1.configure(text="Hello")

def click2():
    label1.configure(text="Hi")

def click3():
    label1.configure(text="bye")
    
label1=Label(window,text=" ")
label1.grid(column=0,row=0)

selected=IntVar()   #this is an integer variable decalration

rad1=Radiobutton(window,text="First" ,value=1,variable=selected,command=click1)
rad1.grid(column=0,row=1)
rad2=Radiobutton(window,text="Second" ,value=2,variable=selected,command=click2)
rad2.grid(column=0,row=2)
rad3=Radiobutton(window,text="Third"  ,value=3,variable= selected,command=click3)
rad3.grid(column=0,row=3)
rad4=Radiobutton(window,text="Third",command=click3)
rad4.grid(column=0,row=4)


def clicked():
    print(selected.get())

button1=Button(window,text ="click me!",command=clicked)
button1.grid(column=3,row=0)



window.mainloop( )
