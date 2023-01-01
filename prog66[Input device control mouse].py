#the start of automation control the mouse and keyboard
import time
import pyautogui
#  pyautogui.displayMousePosition() shows the position of the mouse every second and shows the position pixel's color details in RGB
a,b=0,0
a,b=pyautogui.size()
print(a," , ",b)
time.sleep(2.5)
print(pyautogui.position()) #shows mouse's exact location in pixels at the time of execution
time.sleep(1)
pyautogui.moveTo(30,30)
time.sleep(1)
pyautogui.moveTo(300,450,duration=2)
time.sleep(1)

pyautogui.moveRel(100,-200,duration=2)  #move relative to mouse position 
time.sleep(1)

pyautogui.moveTo(448,117)
print("Get the mouse to the Window bar")
time.sleep(4)

pyautogui.dragTo(300,450,duration=2)
time.sleep(1)

pyautogui.dragRel(148,-333,duration=1)
print("move mouse to minimize")
time.sleep(3)

pyautogui.click(592,124)
time.sleep(1)

pyautogui.moveTo(425,187)
time.sleep(1)

pyautogui.dragTo(x=700,y=900,duration=1.25,button='right') # button chooses which button to use,left/right or primary/secondary
time.sleep(2)

pyautogui.moveTo(813,883,duration=0.5)
time.sleep(1.2)

pyautogui.moveTo(873,779,duration=0.5)
time.sleep(0.5)

pyautogui.click() # you can also put the coordinates for the mouse to click that location, if blank it will click the mouse in its current position

pyautogui.displayMousePosition()


                
