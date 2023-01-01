#improved max

#V1


i=1
maxim=0
while i<11:
    a=int(input("Enter number %d:"%i))
    maxim=max(maxim,a)
    i+=1
print("the maximun is %d"%maxim)


#V2
nums=[]
while len(nums)!=10:
    nums.append(int(input("Enter a number:")))
print(max(nums))
