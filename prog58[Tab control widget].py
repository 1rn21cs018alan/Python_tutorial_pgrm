#adding a tab control widget

from tkinter import *
from tkinter import ttk

window=Tk()
window.title("tab control widget")
window.geometry("500x700")

tab_control=ttk.Notebook(window)

tab1=ttk.Frame(tab_control)
tab_control.add(tab1,text="First")

tab2=ttk.Frame(tab_control)
tab_control.add(tab2,text="second")

tab_control.pack(expand=1, fill= "both")

label1=Label(tab1,text="label 1")
label1.grid(column=0,row=0)


label2=Label(tab2,text="label 2")
label2.grid(column=0,row=0)


window.mainloop()
