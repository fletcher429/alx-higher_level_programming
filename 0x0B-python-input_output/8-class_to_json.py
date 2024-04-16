#!/usr/bin/python3
"""import the json module"""


def class_to_json(obj):
    attributes = obj.__dict__
    serial_attr = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serial_attr[key] = value
    return (serial_attr)
