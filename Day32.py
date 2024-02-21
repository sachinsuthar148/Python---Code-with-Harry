# set methods in python

cities1={"Tokyo","Madrid","Barlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}

# cities3=cities1.union(cities2)
# print(cities3)
# cities1.update(cities2)
# print(cities1)


# cities3=cities1.intersection(cities2)
# print(cities3)
# cities1.intersection_update(cities2)
# print(cities1)


# cities3= cities1.symmetric_difference(cities2)
# print(cities3)
# cities1.symmetric_difference_update(cities2)
# print(cities1)

print(cities1.isdisjoint(cities2))
print(cities1.issuperset(cities2))
print(cities1.issubset(cities2))
cities1.add("Sikwara")
print(cities1)
updateSet={"America","Ramsin"}
cities1.update(updateSet)
print(cities1)
cities1.discard("Sikwara")
print(cities1)
cities1.remove("America")  #rays a error
print(cities1)

item= cities1.pop()
print(item)

# del cities1
cities1.clear()
print(cities1)

