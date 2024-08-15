i=0
#break statement
for i in range(12):
    if(i==10):
        print("Left the loop")
        break
    print("5 x ",i+1," = ",5* (i+1))
i=0
#continue statement
for i in range(12):
    if(i==10):
        print("Skipped the iteration")
        continue
    print("5 x ",i+1," = ",5* (i+1))