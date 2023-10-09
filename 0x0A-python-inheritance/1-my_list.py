#!/usr/bin/python3
"""
    Define a class that inherits from list as base
"""


class MyList(list):
    """
    Define a function that prints the sorted list
    """

    def print_sorted(self):
        sort_list = sorted(self)
        """
            Print the sorted list
        """
        print(sort_list)
