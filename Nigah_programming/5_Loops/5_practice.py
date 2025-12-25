
"""print numbers from 1 to 100
using for and range"""""

for i in range (1,101):
    print(i)
print("END")
"""print numbers from 20 to 1
using for and range"""""

for i in range (20,0,-1):
    print(i)

"""print multiplication table of a number"""
n = int(input("enter number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)