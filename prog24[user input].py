#user input

value=input("Enter your first name:")
age=int(input("Enter your age:"))
if age<=10:
    print("Hi little %s ! Nice to meet you"%value)
elif age<=17:
    print("Howdy %s ! Good day to you"%value)
else:
    print("Hello %s , I wish you a good afternoon"%value)
    
    
