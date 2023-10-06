#!/usr/bin/python3
"""
    Write funtion to return sum of two integers
"""


def add_integer(a, b=98):
    """
    Checks if the the  two numbers are are intgers or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
