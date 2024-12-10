#  Decorators in python 
 

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morninig")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("Hello World")

hello()
#  greet(hello)()

@greet
def add(a,b):
    print(a+b)
add(5,6)

# greet(add)(5,6)