#!/usr/bin/python3
"""import the json module"""
import json


def save_to_json_file(my_obj, filename):
    """convert my_obj to json represantation"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
