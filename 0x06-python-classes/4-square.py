#!/usr/bin/python3
"""
An empty class of a square
"""


class Square:
    """
        The class represents a square object
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a specific size.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.
        """
        return self.__size * self.__size
