x=(int)(input("Enter the number "))
match x:
    case 0:
        print("X is 0")
    case 4:
        print("X is 4")
    case _ if x !=90:
        print("X is not equal to 90")
    case _ if x !=80:
        print("X is not 80")
    case _:
        print("This is the default case")
