#Reverse word order
instr=input("Enter a string:")
splstr=instr.split(" ")
outstr=""
for x in range(0,len(splstr)):
    outstr=splstr[x]+" "+outstr
print(outstr)
