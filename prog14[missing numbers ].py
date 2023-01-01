# missing number program

miss=[]
nums = [1,2,4,6,8,9,10]
a=False
for x in range(1,11):
    if x in nums:
        a=True
    else:
        a=False
        miss.append(x)
print(miss)
    

