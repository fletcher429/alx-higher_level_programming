#!/usr/bin/python3
"""
    Define an empty class called BaseGeometry
"""


class BaseGeometry:
    """
    Define public instance method keep it empty
    """

    def area(self):
        raise NotImplementedError("area() is not implemented")

    """"
        Define a function to check the conditions
    """

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            """
            raise an exception
            """
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            """
            Raise an Exception
            """
            raise ValueError("{} must be greater than 0".format(name))
