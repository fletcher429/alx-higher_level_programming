#!/usr/bin/python3
"""
    Function to add two integers
    Args:

            a - the first intger
            b - the second intger
"""
def add_integer(a, b=98):
    """
        Check if a or b is an int or a float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        # raise the Typerror if the condition is true
        raise TypeError("a must be an integer")
    """
        Check if b is an int or a float
    """
    if not (isinstance(b, int) or isinstance(b, float)):
        # raises the TypeError
        raise TypeError("b must be an integer")
    # casting both arguments into integers
    # returning the sum
    return (int(a) + int(b))


#a = -3.2
#b = -3.2

#print(add_integer(a, b))
