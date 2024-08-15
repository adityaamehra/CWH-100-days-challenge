# taking a and b as required argumnets
def average1(a=9,b=1):
    print("Without any passing of arguments ",((a+b)/(2)))
# taking a and b as default argumnets
def average(a,b):
    print("The average is ",((a+b)/(2)))
# ARBITARY ARGUMENTS
def arb(*num):
    sum=0
    for i in num:
        sum+=i
    return sum
average1(b=4) # here the value of b will be taken as 4 but the value of a will be taken as 9
average((int)(input("Enter the 1st number ")),(int)(input("Enter the 2nd number ")))
average(b=2,a=1)
c=arb(1,2,3,4,4,5,10,6,7,8,8)
print("Printing after returning",c)