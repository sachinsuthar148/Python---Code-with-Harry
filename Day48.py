# Local and Global variables in python

x=10
def hello():
    global x
    x=32
    print(f"the value of x : {x}")
    y=21
    print(f"the value of x : {x}")
    
hello()
print(f"the value of x :{x}")
# print(f"the value of y :{y}")
