# dictionaries in python

dic ={
    "Harry":"Human being",
    "spoon": "object",
    "laptop":"Machine"
}

print(dic["Harry"])
print(dic.get('laptop'))

print(dic.keys())
print(dic.values())
print(dic.items())


for key in dic.keys():
    print(f" value corresponding {key} is {dic[key]}")
    