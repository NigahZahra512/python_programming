"""Range function return a sequence of numbers ,
starting from 0 by default and increment by one """

seq = range(5)
for val in seq:
    print(val)
print("END")


seq = range(2,5)   #range(start and stop)
for val in seq:
    print(val)
print("END")


seq = range(2,10,2)    #range(start , stop ,step)
for val in seq:
    print(val)
print("END")

seq = range(1,10,2)    #range(start , stop ,step)
for val in seq:
    print(val)
print("END")