#modules

import random

print (random.randint(0,5))


list1=[1,2.45,"Jhony",False]
print(random.choice(list1))  


import time

seconds=time.time()
print("number of seconds since 1960 something:",seconds)

print("wait a few seconds")
time.sleep(7.34)                #this is used to delay/pause the program for a defenite amount of time
print("just a few more")
time.sleep(4)
print("almost there")
time.sleep(3)
print("ok i'm done in a sec")
time.sleep(1.25)
print("i'm free now , so what did come here for?")
