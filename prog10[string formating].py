# string operations

stra="Moo says the Cow"
strlenght=len(stra)
print("lenght of the string is ",strlenght)
char=input("enter a character:")
index= stra.index(char)
print("location of '",char,"' in the string is ",index)
count=stra.count(char)
print("the number of times '",char," has appeared in the string is ",count)
#this selects the charcters b,aka characters at 0,1,2,3 for 0:4
#-1 is the first reverse location and 0 is the first front location aka w is at -1 and 15 and m at 0 and -16
#you cant assign values of a string to another by this method
print(stra[0:5])
print(stra[9])
print(stra[-5:-1])
print(stra[0:11:2])
#the first two numbers are the range of characters 0:11 means from 0 to 10
#and 2 means that the charcter loctions are taken at increments of 2 ,aka, 0,2,4,6,8,10
#for 0:11:3 :0,3,6,9
#for 1 its normal,0 is invalid
#for -1 is reverse but the locations must from the reverse directon
print(stra[-4:-16:-1])
#for selecting the enire string leave the first two numbers empty
print(stra[:])
print(stra[::-1])
#case change
print(stra.upper())
print(stra.lower())
# to check if the string starts or ends with a certain set of charcters
print(stra.startswith("Moo"))
print(stra.startswith("Noo"))
print(stra.endswith("now"))
print(stra.endswith("Cow"))
#to split as string based on the occurance of a character into a list
words=stra.split(" ")
word2=stra.split("s")
print(words,";",word2)
