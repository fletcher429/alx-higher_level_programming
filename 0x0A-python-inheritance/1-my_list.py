#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    inti the class
    """
    def __init__(self):
        super().__inti__()
    """
    define a public instance method
    """

    def print_sorted(self):
        """
        sorts the list in ascending order
        """
        result = sorted(self)
        """
        prints the list
        """
        print(result)
