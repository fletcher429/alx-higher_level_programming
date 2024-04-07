#!/usr/bin/python3
def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Not an int")
    return a + b
my_str1 = "David"
my_str2 = " Omondi"

my_str3 = add(my_str1, my_str2)
print(my_str3)