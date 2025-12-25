# program for grading system
marks = int(input("Enter your Marks :"))
if(marks >= 90):
    grade = "A+"
    CGPA = "4.0"
if(marks >= 80 and marks < 90):
    grade = "A"  
    CGPA = "4.0"
if(marks >= 70 and marks < 80):
    grade = "B"
    CGPA = "3.5"
if(marks >= 60 and marks < 70):
    grade = "B"
    CGPA = "3.0"
else:
    grade = "D"
    CGPA = "3.0"

print("Grade of the student ->",grade)
print("CGPA of the student ->",CGPA)