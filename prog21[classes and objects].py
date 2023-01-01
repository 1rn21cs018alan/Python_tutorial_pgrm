# Classes and objects

class myclass():
    word="word-blah"

    def mess(self):   #self must be adde to a class function , i dont know why the self tho(may be deafult object)
        print("This is a function message in the class")

obj1=myclass()
obj2=myclass()
obj2.word="a different message"

print(obj1.word)
print(obj2.word)

obj1.mess()


class vehicle():
    name=""
    kind=""
    colour=""
    value=100.00

    def detail(self):
         description=("this %s , is a %s colour %s that costs $%.2f"%(self.name,self.colour,self.kind,self.value))
         return description


car1=vehicle()
car1.name="Rexton G5"
car1.colour="Crimson"
car1.kind="SUV"
car1.value=1200000.00

car2=vehicle()
car2.name="Nissan Sunny"
car2.kind="Sedan"
car2.colour="Sky Blue"
car2.value=800000.00

print(car1.detail())
print(car2.detail())
