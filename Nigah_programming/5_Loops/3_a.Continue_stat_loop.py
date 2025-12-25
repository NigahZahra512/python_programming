#terminate execution in the current iteration &continue of loop with next iteration
i = 0
while i <= 10:
    if(i == 3):
        i += 1
        continue      #skip the current iteration
    print(i)
    i += 1
print("End of Loop")
