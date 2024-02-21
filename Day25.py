#   Operations on tuple in python


tup=("India","Pakistan","China")

#for adding an element into the tuple
temp= list(tup)
temp.append("Russia")
temp[1]="Finland"
tup= tuple(temp)

print(tup)


print(tup.count("India"))
print(tup.index("China"))