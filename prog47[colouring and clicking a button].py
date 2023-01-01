# button colouring and clicking!


from tkinter import *
window=Tk()
window.title("Button GUI")
window.geometry("500x500")
label1=Label(window,text="press-not this")
label1.grid(column=0,row=0)

def click():                            #This is a command to apply after you click the button
    label1.configure(text="You clicked !")


button1=Button(window,text="clickety click click click")
button2=Button(window,text="clickety click click V2",bg="red",fg="grey" ,command=click)
button1.grid(column=1,row=0)
button2.grid(column=0,row=1)
window.mainloop()
