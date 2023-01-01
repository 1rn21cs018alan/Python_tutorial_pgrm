#birthday dictionary
a={
    'Albert Einstein' : "03/14/1879",
    'Rowan Atkinson' : '01/6/1955',
    'Ada Lovelace' : "12/10/1815",
    'Benjamin Franklin' : "01/17/1706",
    'Donald Trump' : "06/14/1946"
        }
b=input("Enter the peorson to find the birthday:")
d=False
for x in a:
    if x==b:
        print("The birthday of %s is %s "%(b,a[b]))
        d=False
        break
    else:
        d=True
if d : print("forget ",b)
    
    
