#!/usr/bin/python3
"""
    import the required models

"""
"""
    Define a class = Base
"""


class Base:
    """ "
    initiliaze ne class - Base
    """

    _nb_objects = 0

    def __init__(self, id=None):
        """
        arguments
        (id) -> int: the id of the base(new)
        """

        if id is not None:
            """ """
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
