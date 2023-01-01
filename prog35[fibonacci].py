# fibonacci
def fibo(num):
    a,b,c,x=0,1,0,0
    while x<num:
        if(x==0):
            print("0")
            x+=1
        elif(x==1):
            print("1")
            x+=1
        else:
            for x in range(2,num):
                c=a+b
                print(c)
                a=b
                b=c
            x=num
    return 

    
def main():
    num=int(input("Enter the number of fibonacci series you need:"))
    fibo(num)

main()




        
        
        
