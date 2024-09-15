try:
    a=int(input("Enter the number: "))
except:
    print("Hat pagal hai kya")
    a=2
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except:
    print("Sorry some error occured")
print("End of the program")