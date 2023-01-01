#conditional operator

x=2
print(x==2) #equal to
print(x!=2) #not equal to
print(x>2) #greater than
print(x<3) #lesser than
print(x<=2) #less than or equal to  
print(x>=2) #greater than or equal to

name="Power"
age=23
namelist=["Glory","Wealth","Power","Authority"]

if name=="Power" and age==23:
    print( "you have the power of a 23 year old")
if name=="Glory" or age==23:
    print("you may be glory or 23 years old")

a=input() #just to teporarily pause the program(like getch() from c++)
if name in namelist:
    print("You are part of the Cheesy name association")


list1=[1]
list2=[1]
list3=list1
print(list1==list2) #this compares values of the lists
print(list1 is list2) # here both list have same items but they aren't in the same address,so false
print(list1 is list3) # here both lists have same values and address,so True
print(not False)
print((not False)==(False))
