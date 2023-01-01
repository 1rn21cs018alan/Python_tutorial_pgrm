#multiple of 7 not 5
a,b=0,0
c=False
d=False
e=[]
for x in range(2760,2861):
    a=x%7
    b=x%5
    c=(a==0)
    d=(b!=0)
    if c and d:
        e.append(x)
print(e)
