#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
        Gets the attributes of the width
    """

    @property
    def width(self):
        return self.__width

    """
        Manipulate the widht attributes using the setter method

    """

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            return TypeError("width must be an integer")
        elif value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    """
        Gets the attribute of the height
    """

    @property
    def height(self):
        return self.__height

    """
        Manipulate the height attributes using setter method
    """

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            return TypeError("height must be an integer")
        elif value < 0:
            return ValueError("height must be >= 0")
        self.__height = value

    """
        Define a function to calculate the area of the rectangle
    """

    def area(self):
        return self.width * self.height

    """
        Define a function to calculate the perimeter of the rectangle
    """

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    """
        Use the __str__ instance to print the rectangle
        Define the function
    """

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        print_rec = ""

        for _ in range(self.__height):
            print_rec += "#" * self.__width + "\n"
        return print_rec.rstrip()

    """
        Define the __repr__ instance
    """

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
