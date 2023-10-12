#!/usr/bin/python3
"""
    Import json module
"""
import json

"""
    Define a function that loads from json
"""


def load_from_json_file(filename):
    """
    use the with safely open and close the json file
    """
    with open(filename) as json_file:
        """
        returns json decoded file
        """
        return json.load(json_file)
