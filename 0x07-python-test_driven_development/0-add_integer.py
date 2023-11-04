#!/usr/bin/python3
"""
    Define a function to add two numbers
"""


def add_integer(a, b=98):
    """
    returns the add of two ints a and b
    are casted into integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
