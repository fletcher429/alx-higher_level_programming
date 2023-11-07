#!/usr/bin/python3
"""
import the base module
"""
from .base import Base

""""
Create a class named Rectangle
"""


class Rectangle(Base):
    # the class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # define property to access the width's value as if it were an instance variable
    @property
    def width(self):
        return self.__width

    # define setter the method to control how width is assigned values.
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # define property to access the height's value as if it were an instance variable
    @property
    def height(self):
        return self.__height

    # define setter the method to control how height is assigned values.
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__height = value

    # define property to access the x's value as if it were an instance variable
    @property
    def x(self):
        return self.__x

    # define setter the method to control how x is assigned values.
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # define property to access the y's value as if it were an instance variable
    @property
    def y(self):
        return self.__y

    # define setter the method to control how y is assigned values.
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
