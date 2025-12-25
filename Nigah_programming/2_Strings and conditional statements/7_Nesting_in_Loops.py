age = int(input("enter your age:"))
if (age >= 18):
    if(age >= 80):   #NESTING
        print("cannot drive and vote")
    else:
        print("can drive & Vote")

else:
    print("cannot drive & Vote")

