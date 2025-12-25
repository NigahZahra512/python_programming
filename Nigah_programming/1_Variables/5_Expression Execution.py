#string and numerical value can operate together with *

A,B=2,3
Txt="@"
print(2*Txt*3)

#string and string value can operate together with +
A,B="2",3
Txt = "@"
print ((A+Txt)*B)

#Numeric value can operate  with all arthematic operator
A,B=2,3
C=4
print ((A-B)+C)

#Arithematic expression with integer and float will result in float
A,B=2,3.0
C=A*B
print (C)

#Result of division operator with two integer will be float 
A,B=2,3
C=A/B
print (C)

#Reminder is negative when denominator is negative

A,B=2,-3
C=A%B
print (C)

