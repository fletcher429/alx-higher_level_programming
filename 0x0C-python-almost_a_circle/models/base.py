#!/usr/bin/python3
"""
Create a class named Base
"""
class Base:
    __nb_objects = 0
    """
    class constructor
    """
    def __init__(self, id=None):
        """
        checks for the conditions
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
