#!/usr/bin/python3
class Rectangle:
    """
    Initialize the attributes of the class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
        Use the getter method to get the width attributes
    """

    @property
    def width(self):
        return self.__width

    """
        Use the setter method to access and control the width attribute
    """

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            return TypeError("width must be an integer")
        elif value < 0:
            return ValueError("width must be >= 0")

        self.__width = value

    """
        Use the getter method to get/ acces the height attribute
    """

    @property
    def height(self):
        return self.__height

    """
        Use the setter method to acces and manipulate of the height attribute
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
        return self.__width * self.__height

    """
        Define a function to calculate the perimeter of the rectangle
    """

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    """
        Define the __str__ to print the rectangle
    """

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        print_rec = ""

        for _ in range(self.__height):
            print_rec += "#" * self.__width + "\n"

        return print_rec.rstrip()
