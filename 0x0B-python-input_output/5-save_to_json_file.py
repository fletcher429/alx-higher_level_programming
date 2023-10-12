#!/usr/bin/python3
"""
    import json module
"""
import json

"""
    Define a function that writes to a json file
"""


def save_to_json_file(my_obj, filename):
    """
    use with to safely open and close the file
    write to json file to
    """
    with open(filename, "w") as json_file:
        """
        use json.dump() to write and returns py
        """
        json.dump(my_obj, json_file)
