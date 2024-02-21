# If Else Conditional Statements in python

'''
There are four methods to perform conditional statements in python
1. if
2. if-else
3. elif
4. Nested if
Conditional Operators :  >,<,>=,<=,==,!=
'''
    
# age=13
# print(age<10)    #it checks value is true or false


# 1. if

# age = int(input("Enter your age : "))
# if(age>18):
#     print("You can drive")

    
    
   
# 2. if-else

# age = int(input("Enter your age : "))
# if(age>18):
#     print("You can drive")
# else:
#     print("You can not drive")
       
    
# 3. elif

# age = int(input("Enter your age : "))

# if(age<10):
#     print("you can not drive")
# elif(age<14):
#     print("You can drive bicycle")
# elif(age<18):
#     print("You can drive activa")
# elif(age>=18):
#     print("You can drive car")
# else:
#     print("You can not drive")


# 4. Nested if


num= int(input("Enter any number"))

if(num<0):
    print("this is negative number")
elif(num==0):
    print("Number is equal to zero")
else:
    if(num<10):
        print("number is less than 10")
    elif(num<30):
        print("number us less than 30")
    else:
        print("this is positive number")


