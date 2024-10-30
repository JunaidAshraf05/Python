# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

class MyClass:
    def __init__(self, value):
        self._value = value

    # @property
    # def value(self):
    #     return self._value
    
    
    @property
    def ten_value(self):
        return 10* self._value
    
    
    
obj = MyClass(10)
print(obj.ten_value)
