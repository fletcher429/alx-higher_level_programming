#!/usr/bin/python3
"""
An empty class of a square
"""


class Square:
    """
        The class reprsesents a square object
    """

    def __init__(self, size=0):
        """
        Private instance of size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
