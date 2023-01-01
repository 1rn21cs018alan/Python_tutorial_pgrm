# reading a csv file

import csv

with open("D:\Alans-Folder\Miscellaneous\Table2.csv",mode="r") as myfile:
    read1=csv.reader(myfile)
    for row in read1:
        print(row)
