# dictionaries
#they're similiar to array sin c++ and java but use keys and values instead of indexes and values
#ie, array has the data arranged like a list in numerical order but a dictionary uses keys instead of numbers

phonebook1={}        #this is a dictionary and has curly brackets
phonebook1["Car Dealer"]=9792562303  # car dealer is the key and the naumber is the value
phonebook1["Scammer"]=6292562902
phonebook1["null"]=0000000000

print(phonebook1)


phonebook2={                #another way for adding values in groups into a dictionary
    "Car Dealer":9792562303,        #this is a data pair
    "Scammer":6292562902,
    "null":0000000000
    }


print (phonebook2)

for (name,number) in phonebook1.items():
    print("phone number of %s id %.10d"%(name,number))

del phonebook1["null"]                 #a methos to delete an entry in a dictionary
phonebook1.pop("Scammer")       #another deleting method
print(phonebook1)
