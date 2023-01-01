# max of 3 nums
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
maxim=a  #this is one way wihtout functions
if maxim<b:
    maxim=b
if maxim<c:
    maxim=c
print("the max of the three numbers is ",maxim)

maxim=max(a,b,c)  #the function method
print(maxim)
