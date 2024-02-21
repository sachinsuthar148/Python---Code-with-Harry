# Introduction to List in python

'''
1. Enclosed with Square Bracket ( [] )
2. Mutable means can be changed after creation
'''

lst = [2,65,7,"Sachin",True]    #It can contain multiple data types element

print(lst[0])
print(lst[3])
print(lst[4])


if 7 in lst:
    print("Yes")
else:
    print("No")

#Same thing can be applied for string as well
# if "ar" in "Harry":
#     print("Yes")
# else:
#     print("NO")

print(lst[:])   # 0 to last index
print(lst[1:4])
print(lst[-3])
print(lst[len(lst)-3])
print(lst[5-3])
print(lst[2])

    
    
    
#List Comprehension ==> Used to generate new list using a lists,tuple etc


lst2=[i for i in range(4)]
print(lst2)



lst2=[i*i for i in range(10) if(i%2==0)]
print(lst2)