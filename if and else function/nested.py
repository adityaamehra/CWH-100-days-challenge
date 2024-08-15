x=int(input("Enter the number "))
if(x<10):
    print("x is between 1-10")
elif(x>10):
    if(x<15):
        print("x is between 10-15")
    elif(x>15):
        print("x is more than 15")
else:
    print("x is a number")