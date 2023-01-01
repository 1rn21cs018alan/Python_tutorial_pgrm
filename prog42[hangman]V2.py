#hangman
import random
wordsList = ["secret","awkward","bagpipes","croquet","dwarves"]
word=random.choice(wordsList)
wordlen=len(word)
fill=[]
fill=[a for a in word]
guessed=[]
x=0
while True:
    guess=input("Guess a letter or the word: ").lower()
    if guess==word:
        print("you have won")
        break
    elif guess in fill:
        guessed.append(guess)
        temp=word
        for y in fill:
            if y not in guessed:
                temp=temp.replace(y,"_")
        print(temp)
    elif x==10:
        print("you have no more chances")
        break
    else:
        x+=1
input()
        
        
            
            
        
        
