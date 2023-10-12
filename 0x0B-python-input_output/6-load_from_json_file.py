#!/usr/bin/python3
"""
    Import json module
"""
import json

"""
    Define a function that loads from json
"""


def load_from_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)
