#CSV files with custom line-terminaters,delimiters and Quotes

import csv

people=[ ["Name","Age","Gender"],
        ["Spock","29","Male"],
        ["Dave","82","Male"],
        ["Maya","45","Female"] ]

with open("D:\Alans-Folder\Miscellaneous\people.csv",mode="w") as myfile:
    write=csv.writer(myfile)
    write.writerows(people)

with open("D:\Alans-Folder\Miscellaneous\people2.csv",mode="w") as myfile:
    write=csv.writer(myfile,delimiter="|",lineterminator="\n")  #\n is the next line command and the default line-terminator
    write.writerows(people)
with open("D:\Alans-Folder\Miscellaneous\people3.csv",mode="w") as myfile1:
    write=csv.writer(myfile1,delimiter="|",lineterminator="\n\n",quotechar='"',quoting=csv.QUOTE_ALL)  #just adds quotes to all values
    write.writerows(people)
