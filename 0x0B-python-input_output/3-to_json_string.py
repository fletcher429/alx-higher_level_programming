#!/usr/bin/python3
"""
importing the json modules
"""
import json

"""
converts python object to json string
"""


def to_json_string(my_obj):
    """ returns json represntation."""
    return (json.dumps(my_obj))
