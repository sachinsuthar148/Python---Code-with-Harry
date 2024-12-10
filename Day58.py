#  Constructors in python

#Two type of constructor
# 1. Default Constructor
# 2. Parameterized Constructor


# 1. Default Constructor
class Sample:
    def __init__(self):
        print("This is constructoer")

obj1 = Sample()


# 2. Parameterized Constructor
class Sample2:
    def __init__(self, n,o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

    
obj2= Sample2("SACHIN", "DEVELOPER")

obj2.info()