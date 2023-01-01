#writing a dictionary to a csv file
import csv
data= [{"Mountains":"Everest","Height":"8848"},
       {"Mountains":"K2","Height":"8611"},
       {"Mountains":"Ei","Height":"1"},
       {"Mountains":"xiangling","Height":"0"}]

with open("D:\Alans-Folder\Miscellaneous\Table3.csv",mode="w") as myfile:
    fields=["Mountains","Height"]
    writer=csv.DictWriter(myfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
