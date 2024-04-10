class Boy:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"My name is {self.first_name} {self.last_name} and am {self.age} years old"
        
Boy1 = Boy("David", "Omondi", 34)
print(Boy1.__dict__)
