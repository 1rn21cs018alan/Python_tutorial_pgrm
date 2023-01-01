#divisors
a=int(input("Enter a Number:"))
print("the divisors of ",a," are:")
for x in range(1,a+1):
    if ((a%x)==0):
        print(x)
