# no Duplicates
a=[2,34,2,5,6,5,34,8,9,10,8]
b=[]
for something in a:
    if something not in b:
        b.append(something)
print(b)
