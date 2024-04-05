#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an intger")
    for _ in range(size):
        print("#" * size) 
        if size == 0:
            print()
print_square(4)
print("-----------")
print_square(0)
print("------------")
print_square(1)
print_square(20)