def gmean(a,b):
    gmean = ((a*b)**(0.5))
    print(gmean)

def t(a,b):
    if(a==b):
        print("Same")
    elif(a>b):
        print(a,"is greater than",b)
    else:
        print(b,"is greater than",a)

# pass functions , THEY WILL BE WRITTEN AFTERWARDS
def passf(a,b,c):
    pass
for i in range((int)(input("Enter the range "))):
    a=(int)(input("Enter 1st number "))
    b=(int)(input("Enter 2nd number "))
    gmean(a,b)
    t(a,b)

