#creating CSV files
import csv

row=[1,2,3]
rows=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

with open("D:\Alans-Folder\Miscellaneous\Table.csv",mode="w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(row)


with open("D:\Alans-Folder\Miscellaneous\Table2.csv",mode="a") as mofile:
    writer=csv.writer(mofile)
    writer.writerows(rows)
