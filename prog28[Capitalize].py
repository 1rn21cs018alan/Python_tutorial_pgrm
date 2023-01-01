#captialize
a=input("Enter your full name in lower case:")
b=[]
b=a.split(" ")
c=""
for x in range(0,len(b)):
    b[x]=b[x].capitalize()
    c=c+" "+b[x]
print(c)


