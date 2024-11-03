# The syntax for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses, like this:

# class ChildClass(ParentClass):
  
    # class body
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
#   If we want to create a new class for a specific type of animal, such as a dog, we can create a new class named "Dog" that inherits from the Animal class.

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
       
       
       
       