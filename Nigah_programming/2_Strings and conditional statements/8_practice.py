#program to check if a number entered by user us even or odd
num = int(input("Enter  Number:"))
if(num % 2 == 0):
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")


#program to find gratest of 3 number entered by user

a = int(input("enter Ist Number:"))
b = int(input("enter 2nd Number:"))
c = int(input("enter 3rd Number:"))
if(a>= b and a>= c):
    print(a," a is greatest of All")
elif(b>= a and b>= c):
    print(b,"b is greatest of All")
else:
    print(c,"c is greatest of All")

# check if the number ismultiple of 7 or not

num = int(input("enter Number:"))
rem = num % 7
if (rem == 0):
    print("Multiple of 7")
else:
    print(" Not a Multiple of 7")
