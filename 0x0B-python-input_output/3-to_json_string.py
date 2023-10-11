#!/usr/bin/python3
"""
    define a function that returns json represantation of an object
"""
import json

"""
    import json module
"""


def to_json_string(my_obj):
    """
    Returns the json represenation
    """
    return json.dumps(my_obj)
