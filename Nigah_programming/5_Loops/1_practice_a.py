

#print numbers from 20 to 1
n = 20
while n >= 1:
    print(n)
    n -= 1

#print the elements of the following list using loop  : [1,4,9,16,25,36,49,64,81,100]

# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i+=1 
   


#print the elements of the following list using loop  : ["ironman" , "thor" ,"superman" , "batman"]

# list = ["ironman" , "thor" ,"superman" , "batman"]
# idx = 0
# while idx < len(list):
#     print( list[idx])
#     idx +=1 
    
# search for a number x in this tuple using loop :  (1,4,9,16,25,36,49,64,81,100)
tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number:"))
i = 0
while i < len(tuple):
    if(tuple[i] == x):
       print("<<<<<FOUND AT INDX :>>>>" , i)
    else:
       print("<<<< FINDING>>>>")
    i+=1
print("END")