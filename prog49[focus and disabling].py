#Focus and Disabling
from tkinter import *
window=Tk()
window.title("Button GUI")
window.geometry("500x500")
label1=Label(window,text="Enter Name")
label1.grid(column=0,row=0)

text1=Entry(window,width=10) 
text1.grid(column=0,row=1)
text2=Entry(window,width=10,state="disabled")  #disbles the check textox
text2.grid(column=3,row=3)
text3=Entry(window,width=10)        
text3.grid(column=3,row=4)
text3.focus()               #brings the cursor onto the textbox

def click():
    mesg="welcome "+text1.get()
    label1.configure(text=mesg)


button1=Button(window,text="Broken Enter button")
button2=Button(window,text="Enter V2",bg="red",fg="grey" ,command=click)
button1.grid(column=2,row=0)
button2.grid(column=1,row=1)
window.mainloop()
