#!/usr/bin/python3
"""
    Define a function that reads and write a file in utf encoding
    The function returns number of chararcyers written
"""


def write_file(filename="", text=""):
    """
    Use the with to write to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    """
        The function returns the number of characters written
    """
