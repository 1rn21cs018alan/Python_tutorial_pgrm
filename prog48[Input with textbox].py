#Textbox
from tkinter import *
window=Tk()
window.title("Button GUI")
window.geometry("500x500")
label1=Label(window,text="Enter Name")
label1.grid(column=0,row=0)

text1=Entry(window,width=10) #this is the GUI Version of input()
text1.grid(column=0,row=1)

def click():
    mesg="welcome "+text1.get()  #just a string concatination
    label1.configure(text=mesg)


button1=Button(window,text="Broken Enter button")
button2=Button(window,text="Enter V2",bg="red",fg="grey" ,command=click)
button1.grid(column=2,row=0)
button2.grid(column=1,row=1)
window.mainloop()
