#!/usr/bin/python3
"""
function that append text at the EOF and returns the number of characters
"""


def append_write(filename="", text=""):
    """
    using the with function to open the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return (len(text))
