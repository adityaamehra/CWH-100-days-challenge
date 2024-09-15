def fun1():
    try:
        a=[3,4,5,5]
        i=int(input("Enter the index :"))
        print(a[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("This block of code will always work")
    print("I am always executed part 2") # This will not be executed as after returning this will never be reached

x=fun1()
print(x)

