#!/usr/bin/python3
"""
    Define an empty class called BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
    Define the class
"""
class BaseGeometry:
    """
        Initiliaze the objects
    """
    def __init__(self, width, height):
        """
            args:
            width(w)
            height(h)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
