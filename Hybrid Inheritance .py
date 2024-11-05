# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.


# Here's the syntax for defining a hybrid inheritance class hierarchy:


class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass
