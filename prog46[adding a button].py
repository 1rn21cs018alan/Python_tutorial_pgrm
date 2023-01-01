#adding a button


from tkinter import *
window=Tk()
window.title("Button GUI")
window.geometry("500x500")
label1=Label(window,text="press-not this")
label1.grid(column=0,row=0)

button1=Button(window,text="clickety click click click")
button2=Button(window,text="clickety click click click")
button1.grid(column=1,row=0)
button2.grid(column=0,row=1)
window.mainloop
()
