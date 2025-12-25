# #break is Used to Terminate the loop when encountered
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#        break
#     i += 1
# print("End of Loop")




# search for a number x in this tuple using loop :  [1,4,9,16,25,36,49,64,81,100]

tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number:"))
i = 0
while i < len(tuple):
    if(tuple[i] == x):
       print("<<<<<FOUND AT INDX :>>>>" , i)
       break                 # Terminates the loop 
    else:
       print("<<<< FINDING>>>>")
    i+=1
print("END")
    
