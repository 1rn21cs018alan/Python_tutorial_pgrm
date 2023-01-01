#check button

from tkinter import *
from tkinter.ttk import *

window=Tk ()
window.title ("Checkbox")
window.geometry ("500x600")

checkvalue = BooleanVar ()
checkvalue.set  (True)  #this makes the default state of the button to be True aka, checked
                                #can also be written as checkvalue.set(1)  1 for true and 0 for false

check = Checkbutton (window ,text="Choose a button" ,var=checkvalue)
check.grid (column=0 ,row=0)

window.mainloop( )
