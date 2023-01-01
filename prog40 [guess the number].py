#Guess the NUmber
import random
print("Guess the Chosen number from 1 to 9 ")
real=random.choice(range(1,10))
while True:
    guess=int(input())
    if guess<real:
        print("Too Low")
    elif guess>real:
        print("Too High")
    else:
        print("Correct")
        break
    print("Guess again")
input()
