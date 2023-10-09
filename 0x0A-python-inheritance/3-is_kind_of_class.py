#!/usr/bin/python3
"""
    Define a function that returns True if the object is an insatnce of
    or if the object is an instance of a class that inherited from the
    specified class, or false
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True or False
    """
    return isinstance(obj, a_class)
