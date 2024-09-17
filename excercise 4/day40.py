s=input("Enter the message\n")
a=int(input("Do you want to encode or decode the message\n"))
if a==1:
    c=""
    b=s.split(" ")
    for x in b:
        if len(x)<=4 :
            s2=x[::-1]
        else:
            s2="axc"+x[1:]+x[0]+"wuk"
        c+=" "+s2
    print(f"The encoded sentence is {c}")
elif a==2:
    c=""
    b=s.split(" ")
    for x in b:
        if len(x)<=4 :
            s2=x[::-1]
        else:
            s2=x[-4:-3]+x[3:-4]
        c+=" "+s2
    print(f"The decoded message is : {c}")
