import random

name_list = ["Ada", "Harry", "Elon", "Jane"]
surname_list = ["Lovelace", "Musk", "Potter", "Doe"]

    

#for num in range(1,91):    
#    
#    string = " - " + random.choice(name) + " " + random.choice(surname) #+ " - "
#    
#    statement = ""
#    
#    if num % 3 == 0:
#        statement = "LOAN"
#    if num % 5 == 0:
#        statement = statement + " Pending"
#    if num % 5 != 0 and num % 3 != 0:
#        statement = "no data"
#    
#    
#    print(str(num)+string+statement)
    
    
#BONUS2 
for num in range(1,91):    
    
    full_name = random.choice(name_list) + " " + random.choice(surname_list)
    
    string = " - " + full_name + " - "
    
    statement = ""
    
    if num % 3 == 0:
        statement = "LOAN"
    if num % 5 == 0:
        statement = statement + " Pending"
    if num % 5 != 0 and num % 3 != 0:
        statement = "no data"
    if full_name == "Ada Lovelace" or full_name == "Elon Musk":
        statement = "LOAN"
        
    print(str(num)+string+statement)
