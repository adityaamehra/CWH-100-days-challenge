try:
    a=int(input("Enter the number: "))
except ValueError:
    print("Hat pagal hai kya")
    a=2
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except ValueError:
    print("Sorry some error occured")
print("End of the program")


try:
    num=int(input("Enter a number: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Error 1")
except IndexError:
    print("Error 2")