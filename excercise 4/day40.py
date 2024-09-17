s=input("Enter the message\n")
a=int(input("Do you want to encode or decode the message\n"))
if a==1:
    if len(s)<=4 :
        s2=s[::-1]
    else:
        s2="wce"+s[1:]+s[0]+"wce"
    print(f"The encoded message is : {s2}")
elif a==2:
    if len(s)<=4 :
        s2=s[::-1]
    else:
        s2=s[-4:-3]+s[3:-4]
    print(f"The decoded message is : {s2}")
