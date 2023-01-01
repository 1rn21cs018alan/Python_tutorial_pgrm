#reading a TXT File
with open("D:\Alans-Folder\Miscellaneous\c.txt",mode="r") as MyFile:
    #this is the reading mode,pretty self explanatory
    for x in MyFile:
        print(x)
