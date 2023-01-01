#prime number
a=int(input("Enter a Number:"))
b=False
while True:
    for x in range(1,a):
        if (((a%x)==0) and (x!=1) ):
            b=True
    if b==True:
        print("%d is not a prime number"%a)
    else:
        print("%d is a prime number"%a)
    break
    
