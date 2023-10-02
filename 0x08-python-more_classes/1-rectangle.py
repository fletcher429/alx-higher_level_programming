#!/usr/bin/python3
"""
    This is a RECTANGLE class
"""


class Rectangle:
    """
    Create empty Rectangle Object
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            return TypeError("width must be an integer")
        elif value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            return TypeError("height must be an integer")
        elif value < 0:
            return ValueError("height must be >= 0")
        self.__height = value
