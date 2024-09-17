a=input("Enter any value between 5 and 9\n")
if a== "quit":
    exit(0)
else:
    a=int(a)
if a<5 or a>9:
    raise ValueError("Enter a value between 5 and 9")
else:
    print(f"a is {a}")

#Defining custom error

