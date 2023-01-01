# else clause with loops


count=0                                                                           
while count<=10:                                           #this is considerd as one loop                 
    print( count)                                               # the else statement is run after the loop                           
    count+=1                                                  #          condition returns false                    
else:                                                             #                          
    print("count value has reached ",count)          #                                            

for i in range(1,20):                           #   here the for loop and the else is considered as the same loop
    print (i)                                        #   so when a break statement is triggered the else statement
    if i>=18:                                      #            is also skipped 
        break                                      #    continue has no effect since it only terminates the current iteration
else:                                               #               while break terminates the whole loop
    print("Loop terminated")                #    
