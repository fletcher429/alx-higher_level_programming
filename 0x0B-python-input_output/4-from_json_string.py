#!/usr/bin/python3
"""import the json moduel"""
import json


def from_json_string(my_str):
    """returns  python obj rep by the json string"""
    return json.loads(my_str)
