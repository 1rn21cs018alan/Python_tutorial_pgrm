# File reading and over lap
a=[]
b=[]
over=[]
with open("D:/Alans-Folder/Download/a.txt") as file1:  #this reads the input file from given loctation and stores its value in"file1"
    line1=file1.readline()  #theis reads a line from the variable file1 where a.txt is stored
    while line1:            # this stays true until line has no value, so it takes null aka, false.
        a.append(int(line1))
        line1=file1.readline()   #this comand reads the line where the cursor is. it the goes to the next line but doesnot read them
with open("D:/Alans-Folder/Download/b.txt") as file2:
    line2=file2.readline()
    while line2:
        b.append(int(line2))
        line2=file2.readline()
for x in a:
    if x in b:
        over.append(x)
print(over)
