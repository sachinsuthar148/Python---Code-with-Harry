# f-strings in python


'''
two methods -> .format method and using f".."
'''


letter = "Hey my name is {1} and i am from {0}"
city="sikwara"
name="Sachin"

print(letter.format(city,name))

print(f"Hey my name is {name} and i am from {city}")


price=9.43443
txt= f"Hey today price is {price:.2f} dollors"
print(txt)


print((f"{12*3}"))