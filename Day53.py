# Map, Reduce and Reduce function in  python
# These are higher order function


# MAP FUNCTION

list1 =[1,2,3,4,5,6,7]
def cube(x):
    return x*x*x

newList1 = list(map(cube,list1))
print(newList1)
newList1 = list(map(lambda x: x*x,list1)) # we can pass lambda function also.
print(newList1)


# FILTER FUNCTION

list2=[23,4,5,6,34,243]
newList2 = list(filter(lambda x:x>6,list2))
print(newList2)


# REDUCE FUNCTION
from functools import reduce

list3=[1,2,3,4,5,6,7,8,9,10]

sum= reduce(lambda x,y: x+y,list3)
print(sum)   