# Lambda function in python

'''
Anonymous function without the name
defined by the lambda function
'''

def double(x):
    return x*2;
print(double(4))

# Instead of writing this ... we can write

double1= lambda x:x*2
print(double(9))

cube = lambda x:x*x*x
print(cube(3))


def appl(fn, value):
    return fn(value)

print(appl(lambda x:x*4,90))