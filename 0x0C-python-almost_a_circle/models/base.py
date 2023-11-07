#!/usr/bin/python3


"""
This is the Base module, which defines the Base class.
"""


class Base:

    """
    Represents the Base class.

    Attributes:
        __nb_objects (int): Class attribute to keep track
        id (int): Unique identifier for the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The unique identifier. Defaults to None.

        Conditions:
            - If id is provided, it is used as the object's id.
            - If id is not provided, a new unique id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
