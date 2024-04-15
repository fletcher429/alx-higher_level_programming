# PYTHON INHERITENCE
- Inheritence allows us to define a class that inherits all the methods and properties from another class

1. Parent Class - Class being inherited from
2. Child Class - is the class that inherits from another class also derived class.

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)
        
x = Person("John", "Doe")
x.printname()

class Student(Person): # Inherits from parent class
    pass