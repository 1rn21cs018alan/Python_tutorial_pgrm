#writing to a TXT File
with open("D:\Alans-Folder\Miscellaneous\c.txt",mode="w") as MyFile:
    #this is the write mode that writes the note from scratch
    for x in range(1,111):
        MyFile.write(str(x)+"\n")
        
with open("D:\Alans-Folder\Miscellaneous\c.txt",mode="a") as MyFile:
    #this is append mode that adds strings into the written file
    for x in range(20,41):
        MyFile.write(str(x)+"   ")
