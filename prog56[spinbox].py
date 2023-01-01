#spinbox
from tkinter import *
window=Tk()
window.title("Spinbox")
window.geometry("500x300")

spin=Spinbox(window, from_=0 , to=100 ,width =5)   #in Tkinter "from_" is a keyword and "from" is a different python keyword
spin.grid(column=0,row=0)

spi=Spinbox(window, values=(3,5,7,9,12,345,67,234,43),width=5)
spi.grid(column=0,row=1)


var=IntVar()
var.set(55)
sp=Spinbox(window, from_=0 , to=100 ,width =5,textvariable=var)
sp.grid(column=0,row=2)





window.mainloop()
