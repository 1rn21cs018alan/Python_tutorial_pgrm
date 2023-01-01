#hangman
import random
import string
wordsList = ["secret","awkward","bagpipes","croquet","dwarves"]
word=random.choice(wordsList)
wordlen=len(word)
fill=[]
for y in range(0,wordlen):
    fill.append("_")
fill2=""
x=0
while True:
    guess=input("Guess a letter or the word: ").lower()
    x+=1
    if guess==word:
        fill2=word
    elif len(guess)==1:
        z=0
        while z<wordlen:
            if (word[z]==guess) and (fill[z]!=guess):
                fill[z]=guess
                fill2="".join(fill)
                print(fill2)
                break
            z+=1
    if fill2==word:
        print("you have won")
        break
    if x==10:
        break
if x==10:
    print("you have no more chances")
input()
        
        
            
            
        
        
