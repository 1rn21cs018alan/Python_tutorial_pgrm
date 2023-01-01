#break ,continue statement

count=0;
while True:  #While True  is an infinite loop since True is an unchanging constant
    print(count)
    count += 1
    if count>=5:
        break

for x in range(10):
    if (x%2)==0:
        continue
    print(x)
    
