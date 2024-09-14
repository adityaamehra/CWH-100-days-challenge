#Factorial finding using recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(3))
#Fibonnaci series using recursion
def fibo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo((int)(input())))