# Fuctions in python

'''
There are two types of functions in python
1. Built-in functions => max(),min(), sum(),range() etc.
2. User defined function => with the help of "def" keyword
'''


def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    else:
        print(b,"is greater then",a)
        
def isLesser(a,b):
    pass   #if we have decleared a function and body doesn't exit then we use "pass" keyword

calculateGmean(10,4)
isGreater(34,1)
isGreater(34,45)