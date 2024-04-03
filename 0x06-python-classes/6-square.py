#!/usr/bin/python3
"""
An empty class of a square
"""


class Square:
    """
    The class represents a square object
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a specific size and position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the specified position.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


square = Square(5, (2, 1))
square.my_print()
