#Finally keyword in Exception Handling

def func1():
    try:
        a=[32,43,2,12,3]
        x=int(input("Enter the index"))
        print(a[x])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")
    
x=func1()
print(x)