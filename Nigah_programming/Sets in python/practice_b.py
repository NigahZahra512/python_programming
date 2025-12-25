#Enter marks of 3 subjects from user and store them in ductionary .
# start with empty dictionary and add one by one.

marks = {}

x = int(input("Enter phy marks:"))
marks.update({"phy" : x })

x = int(input("Enter Maths marks:"))
marks.update({"Maths" : x })

x = int(input("Enter Bio marks:"))
marks.update({"Bio" : x })

print(marks)