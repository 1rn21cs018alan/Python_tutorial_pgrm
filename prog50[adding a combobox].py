#adding a combo box

from tkinter import *
from tkinter.ttk import *
def click():
    msg="You Chose "+combo.get()
    label2.configure(text=msg)

window=Tk() 
window.title("Combobox program")    #this gaive a drop down list
window.geometry("500x700")

label1=Label(window,text="Choose a number: ")
label1.grid(column=0,row=0)

label2=Label(window)
label2.grid(column=0,row=2)

combo=Combobox(window)
combo['values']=(1,2,3,4,5,"Moo Goat")  #put values not Values
combo.current(1)    #this is the index value not actual value and combo[1]=2
combo.grid(column=0,row=1)

button1=Button(window,text="enter",command=click)
button1.grid(column=1,row=1)
window.mainloop()
