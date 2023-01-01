#palindrome number <3000 also a multiple of 13
a=""
maxnum=0
for x in range(1,3001):
    if(x%13==0):
        a="%d"%x
        b=False
        for y in range(0,(len(a))):
            c=a[y]
            d=a[len(a)-(y+1)]
            if c!=d:
                b=True
        if b:
            continue
        else:
            maxnum=x
print(maxnum) #answer should be 2002
                    
