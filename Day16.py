# Match Case statement in python


x= int(input("Enter any number:"))

match x:
    case 0:
        print("X is 0")
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 3:
        print("X is 3")
    case _ if x==80:
        print("Number is 80")    
    case _:
        print(x)
    
    