""" using for :
print the element of following list using loop
[1 , 4 , 9 , 16 ,25, 36 , 49 , 64 , 81 , 100]
"""
Nums =[1 , 4 , 9 , 16 ,25, 36 , 49 , 64 , 81 , 100]
for val in Nums:
    print(val)


""" using for :
search for a number x in this tuple using loop
(1 , 4 , 9 , 16 ,25, 36 , 49 , 64 , 81 , 100)
"""
nums =(1 , 4 , 9 , 16 ,25, 36 , 49 , 64 , 81 , 100)
x = int(input("Enter Number :"))

idx = 0
for val in nums :
    if(val == x):
        print("Number Found at index :" ,idx)
    idx += 1


