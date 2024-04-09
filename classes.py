#!/usr/bin/python3
class Boy:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def get_name(self):
        return print("My name is: {} and am {} years old. My height is {}".format(self.name, self.age, self.height))
    
Boy1 = Boy("Daved", 21, 6)

Boy1.get_name()
print(list(range(2, 10, 2)))
a = "Python is cool"
print(a[7:-5])
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
print(a.get('friends')[-1].get("name"))