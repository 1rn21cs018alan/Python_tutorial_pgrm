#rock paper siz shoooting timeeeee
import random
import string
import time
print("Welcome to the Rock Paper Scissor Game")
choose=["Rock","Paper","Scissor"]
print("Choose any one of these:",choose)
print("Rock, Paper, Scissor Shoot")
time.sleep(1.5)
a=input("You choose ").lower()
b=random.choice(choose)
time.sleep(1.5)
print("Computer Choose ",b)
b=b.lower()
time.sleep(1.5)
if a==b:
    print("Draw")
elif (a=="rock") and (b=="scissor"):
    print("Player Wins")
elif (a=="rock") and (b=="paper"):
    print("Computer Wins")
elif (a=="paper") and (b=="rock"):
    print("Player Wins")
elif (a=="paper") and (b=="scissor"):
    print("Computer Wins")
elif (a=="scissor") and (b=="rock"):
    print("Computer Wins")
elif (a=="scissor") and (b=="paper"):
    print("Player Wins")


def rps():
    choose=["Rock","Paper","Scissor"]
    print("Rock, Paper, Scissor Shoot")
    time.sleep(1)
    a=input("You choose ").lower()
    b=random.choice(choose)
    time.sleep(1.5)
    print("Computer Choose ",b)
    b=b.lower()
    time.sleep(1.5)
    if a==b:
        print("Draw")
    elif (a=="rock") and (b=="scissor"):
        print("Player Wins")
    elif (a=="rock") and (b=="paper"):
        print("Computer Wins")
    elif (a=="paper") and (b=="rock"):
        print("Player Wins")
    elif (a=="paper") and (b=="scissor"):
        print("Computer Wins")
    elif (a=="scissor") and (b=="rock"):
        print("Computer Wins")
    elif (a=="scissor") and (b=="paper"):
        print("Player Wins")
    else:
        print("Error")
    return

def main():
    time.sleep(1)
    choice=["Y","N"]
    x=1
    while True:
        x+=1
        print("Do you wnat to play again?",choice)
        a=input().upper()
        if a=="Y":
            if x==8:
                print("Hey, how much more will we do this....")
                time.sleep(4)
            elif x==12:
                print("Are you a sweat or some thing lemme rest")
                time.sleep(4)
            elif x==15:
                print("NOPE! I'm outta here Syke!")
                time.sleep(4)
                return
            rps()
            time.sleep(1.5)
        elif a=="N":
            break
        else:
            print("Error")
    return
        
main()        



    
