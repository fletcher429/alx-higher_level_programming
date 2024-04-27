#!/usr/bin/python3
"""Class Base"""
class Base:
    """private class attribute"""
    __nb_objects = 0
    """
    Class constructor
    Args: 
        Self - reffrence to the current of the class
        id  - class attrinute
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects by 1 if is None
            Base.__nb_objects += 1
            # set the value of id to __nb_objects
            self.id = Base.__nb_objects