#creating a message box

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Message Box")
window.geometry("500x400")

def click1():
    messagebox.showinfo("Normal Message","Message content")
    
button1=Button(window,text="Normal",command=click1)
button1.grid(column=0,row=0)

def click2():
    messagebox.showwarning("Warning Message","Be ware of the dog!")
    
button2=Button(window,text="Warning!",command=click2)
button2.grid(column=0,row=1)

def click3():
    messagebox.showerror(" Error Message","Error")
    
button3=Button(window,text="Error",command=click3)
button3.grid(column=0,row=2)

def click4():
    result=messagebox.askquestion("Question"," Do you do multi pulls in Genshin?")
    print(result)
    
button4=Button(window,text="Question 1",command=click4)
button4.grid(column=0,row=3)

def click5():
    result=messagebox.askyesno("Question V2","Are tomatoes fruits?")
    print(result)
    
button5=Button(window,text="question 2",command=click5)
button5.grid(column=0,row=4)

def click6():
    result=messagebox.askyesnocancel("Optional question","Can an ion thruster accelerate using Heavy Metal ions?")
    print(result)
    
button6=Button(window,text="Cancellable question",command=click6)
button6.grid(column=0,row=5)

def click7():
    result=messagebox.askokcancel("permission type","Do you agree to the Privacy Terms")
    print(result)
    
button7=Button(window,text="Continue",command=click7)
button7.grid(column=0,row=6)

def click8():
    result=messagebox.askretrycancel("You Failed!","Try again?")
    print(result)
    
button8=Button(window,text="Try Becoming Allmight",command=click8)
button8.grid(column=0,row=7)






window.mainloop()
