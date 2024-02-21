#Exception Handling in python

# try:
#     a= input("Enter a number:")
#     print(f"The table of {a} is :")

#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {(int(a)*int(i))}")
# except Exception as e:
#     print(e)
#     print("Invalid user input")
    
    
try:
    a=[23,43]
    x=int(input("Enter index:"))
    print("Entered number is",x)
    print(a[x])
except ValueError:
    print(ValueError)
except IndexError:
    print(IndexError)
    