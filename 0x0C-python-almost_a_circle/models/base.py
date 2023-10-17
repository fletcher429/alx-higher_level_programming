#!/usr/bin/python3
"""
    Define a class called a base
"""
class Base:
    """
        inititilize __nb_objects to zero
    """
    __nb_objects  = 0
    """
        init the attributes
    """

    def __init__(self, id =None):
        """
            check for the conditions
        """
        """
            args(id) - the id
        """
        if id is not None:
            self.id  = id
        else:
            """
                increement the __nb_objects by 1
            """
            Base.__nb_objects += 1
            """
                update the id with __nb_objects
            """
            self.id  = Base.__nb_objects

