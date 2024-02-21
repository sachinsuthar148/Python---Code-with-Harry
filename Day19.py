#Break and continue in python

while True:
    i=int(input("Enter a number between 1 to 10:"))
    if(i==4):
        print("you have entered correct number")
        break
    if(i==0):
        continue
    if(i>10):
        print("Enter valid number between 1 to 10")
    if(i<=10 and i>=1):
        print("value of i is",i)