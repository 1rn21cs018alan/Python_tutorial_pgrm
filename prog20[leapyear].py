# leap year

def leapyear(year):
    leap=year%4
    if leap==0:
        print("year %d is a leap year"%year)
    else:
        print("year %d is not a leap year"%year)
    
    return

def main():
    a=int(input("Enter the Year:"))
    leapyear(a)


main()
