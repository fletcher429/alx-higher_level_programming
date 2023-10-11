#!/usr/bin/python3
"""
    Defines a function that opens as file with 'with'
    keyword
"""


def read_file(filename=""):
    """
    opens the file in read only mode
    """
    with open(filename, "r", encoding='UTF-8') as f:
        item = f.read()
    print(item)
