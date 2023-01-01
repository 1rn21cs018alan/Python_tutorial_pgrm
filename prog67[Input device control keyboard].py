#the start of automation control the mouse and keyboard
import time
import pyautogui
import pyperclip

# print(pyautogui.KEYBOARD_KEYS)  prints all available keypresses' names


pyautogui.typewrite("abcd efgh ithsk",interval=0.1)
pyautogui.typewrite(['\n','a','a','left','e','b','\n','volumeup','volumeup','volumeup',\
                     'volumedown','volumedown','volumedown','s','u','right','\n'],interval=0.15)
pyautogui.typewrite("hi",interval=0.01)
time.sleep(1)
pyautogui.press('space')
time.sleep(1)
pyautogui.typewrite("hello",interval=0.01)

pyautogui.hotkey('shift','up',interval=0.5) #presses down all the keys simultaneously or with interval if mentioned
time.sleep(0.5)

pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','end')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyperclip.copy("This is copied text")
pyautogui.hotkey('ctrl','v')

