# Python Inheritance Project

This Python project explores the concept of inheritance, using various classes and methods to demonstrate how classes can inherit attributes and behaviors from one another. Here's a breakdown of the tasks and files included in this project, along with corresponding emojis:

🔍 **Task 0: Lookup Function**
- The `lookup` function returns a list of available attributes and methods of an object.

📄 File: `0-lookup.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
```

---

📚 **Task 1: MyList Class**
- The `MyList` class inherits from the built-in `list` class and adds a `print_sorted` method to print the list in ascending order.

📄 File: `1-my_list.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
```

---

🔄 **Task 2: is_same_class Function**
- The `is_same_class` function checks if an object is exactly an instance of the specified class.

📄 File: `2-is_same_class.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
```

---

✅ **Task 3: is_kind_of_class Function**
- The `is_kind_of_class` function checks if an object is an instance of, or if it inherits from, the specified class.

📄 File: `3-is_kind_of_class.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
```

---

🔗 **Task 4: inherits_from Function**
- The `inherits_from` function checks if an object is an instance of a class that directly or indirectly inherits from the specified class.

📄 File: `4-inherits_from.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
```

---

📐 **Task 5: BaseGeometry Class**
- The `BaseGeometry` class is an empty class that serves as a base for other classes.

📄 File: `5-base_geometry.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
bg = BaseGeometry()
print(bg)
print(dir(bg))
```

---

📏 **Task 6: Improve Geometry**
- The `BaseGeometry` class is updated with an `area` method that raises an exception with the message "area() is not implemented."

📄 File: `6-base_geometry.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
bg = BaseGeometry()
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

---

🔢 **Task 7: Integer Validator**
- The `BaseGeometry` class is further improved with an `integer_validator` method that validates input values.

📄 File: `7-base_geometry.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
bg = BaseGeometry()
bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)
```

---

📏 **Task 8: Rectangle Class**
- The `Rectangle` class inherits from `BaseGeometry` and includes instantiation with width and height, with validation.

📄 File: `8-rectangle.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
r = Rectangle(3, 5)
print(r)
print(dir(r))
```

---

📏 **Task 9: Full Rectangle**
- The `Rectangle` class is enhanced to include an `area` method and a customized string representation.

📄 File: `9-rectangle.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
r = Rectangle(3, 5)
print(r)
print(r.area())
```

---

◾ **Task 10: Square #1**
- The `Square` class inherits from `Rectangle` and is instantiated with a size parameter.

📄 File: `10-square.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
s = Square(13)
print(s)
print(s.area())
```

---

◾ **Task 11: Square #2**
- The `Square` class is further improved to include a customized string representation.

📄 File: `11-square.py`

📂 Directory: `0x0A-python-inheritance`

👇 Usage example:
```python
s = Square(13)
print(s)
print(s.area())
```

🚀 This Python Inheritance Project demonstrates the power and flexibility of object-oriented programming by using inheritance to create classes with shared behaviors and attributes. Enjoy exploring and learning from these tasks! 🐍