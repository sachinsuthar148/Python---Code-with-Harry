#Ennumerate function in python


marks=[1,34,56,34,23,87,54,34,231]

index=0
for mark in marks:
    print(mark, end=" ")
    if(index == 4):
        print("nice")
    index +=1
    

print("\n")
    
for index,mark in enumerate(marks):
    print(mark,end=" ")
    if(index  == 4):
        print("Enumurate function testing")