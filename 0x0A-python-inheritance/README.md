# PYTHON INHERITANCE

Inheritance allows us to define a class that inherits all the methods and properties from another class.

- **Parent Class:** Class being inherited from.
- **Child Class:** The class that inherits from another class, also known as the derived class.

## PARENT CLASS

```python
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
  
    def printname(self):
        print(self.fname, self.lname)

x = Person("John", "Doe")
x.printname()
# Creating A child class to inherit from the parent class
class Student(Person):  # Inherits from the parent class
    pass

## Making the child calls overide __int__() of the parent class

```python

class Student(Personn):
    def ___int__(self, fname, lname)
    ## This overrides the properties from the Parent class
```

- If we want to keep the properties we can use Person. to acces its 
properties

```python
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
```

Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

### THE SUPER FUNCTION

Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```

- By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

```python
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)





