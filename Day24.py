# Tuples in python


# tuples are immutable --> can not be change

tup=(34,45,23,4,6,2)
print(type(tup),tup)

print(len(tup))
print(tup[1])
print(tup[2])
print(tup[3])

print(tup[:])

if 34 in tup:
    print("YES")
else:
    print("NO")