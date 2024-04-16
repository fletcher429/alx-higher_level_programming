#!/usr/bin/python3
"""
    Function to open and read a file
    Args:
        filename - the filename
"""


def read_file(filename=""):
    """
    Use the with top open file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        f = f.read()
        print(f)
