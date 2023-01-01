# rock paper scissor improved version(self)
import random
from tkinter import *
from tkinter import messagebox

def msg(val1,val2,res):
    messagebox.showinfo("Result","Computer chose : %s \n You chose : %s \n %s"%(val2,val1,res))
    return
    

def Rock():
    choose=["Rock","Paper","Scissor"]
    a=random.choice(choose)
    if a=="Rock":
        b="It's a draw"
    elif a=="Paper":
        b="You lost"
    else:
        b="You won"
    msg("Rock",a,b)
    return


def Paper():
    choose=["Rock","Paper","Scissor"]
    a=random.choice(choose)
    if a=="Rock":
        b="You won"
    elif a=="Paper":
        b="It's a draw"
    else:
        b="You lost"
    msg("Paper",a,b)
    return


def Scissors():
    choose=["Rock","Paper","Scissor"]
    a=random.choice(choose)
    if a=="Rock":
        b="You lost"
    elif a=="Paper":
        b="You won"
    else:
        b="It's a draw"
    msg("Scissors",a,b)
    return




window=Tk()
window.geometry("270x60")
window.title("Rock, Paper, Scissors")


label1=Label(window,text="Choose between one of the three")
label1.grid(column=2,row=0)

button1=Button(window,text="Rock", height=2, bg="black", fg="yellow", command=Rock)
button1.grid(column=1,row=1)

button2=Button(window,text="Paper",height=2, bg="white", fg="blue", command=Paper)
button2.grid(column=2,row=1)

button3=Button(window,text="Scissors",height=2, bg="grey", fg="white", command=Scissors)
button3.grid(column=3,row=1)





window.mainloop()
