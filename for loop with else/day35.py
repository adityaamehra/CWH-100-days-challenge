# When the loop's execution is completed successfully without breaking then only the else block is executed

for i in range(6):
    print(i,end=' ')
else:
    print("Sorry no i")
i=0
while (i<7):
    print(i,end=' ')
    i+=1
else:
    print("No i")