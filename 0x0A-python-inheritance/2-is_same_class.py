#!/usr/bin/python3
"""
    Define a function returns True if the object is exactly an instance of the specified class ;
    otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns TRUE or FLASE
    """
    if type(obj) == a_class:
        return True
    return False
