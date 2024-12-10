# Getters and setters in python


class MyClass:
    def __init__(self,value):
        self._value = value
    
    def info(self):
        print(f"value is {self._value}")

    @property #getters
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self,newValue):
        self._value = newValue/10

obj = MyClass(10)
obj.info()
print(obj.ten_value)

obj.ten_value = 340
obj.info()
