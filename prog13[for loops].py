#for loops


primes=[2,3,5,7,11,13,17,19,23,29,31,37,41]
for prime in primes:
    print(prime)

print()

for x in range(8):  #range is a set of whole numbers and this will show 0-7 but not 8
    print(x)


#the prime number loop
for y in range(100):
    a=False
    for z in range(100):
        if (y!=z) and (y>1) and (z>1) :
            if ((y%z)==0):
                a=True
    if a==False:
        print(y)
print()    
for x in range(5,9):
    print(x)

print()
for x in range(5,14,2):
    print(x)
