# palindrome
a=""
b=""
c=False
str=input("Enter a word:")
for x in range(0,len(str)):
    a=str[x]
    b=str[(-1-x)]
    if a!=b:
        c=True
if c:
    print("%s is not a plaindrome"%str)
else:
    print("%s is a palindrome"%str)
    
