#reading a dictionary from a csv file

import csv

with open ("D:\Alans-Folder\Miscellaneous\Table3.csv",mode="r") as myfile:
    reader=csv.DictReader(myfile)
    line=1
    for row in reader:
        if line==1:
            print(f'{",".join(row)}')
            line+=1
        print(f'{row["Mountains"]},{row["Height"]}')
