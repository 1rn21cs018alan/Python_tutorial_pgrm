#factorial

a=int(input("enter a number:"))
b=1
for x in range (1,(a+1)):
    b*=x
print("the factorial of %d is %d"%(a,b))
