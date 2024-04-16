#!/usr/bin/python3
"""
defines a function that writes to the file
"""


def write_file(filename="", text=""):
    """
    using with open to effectively close the file after use to avoid the leaks
    """
    with open(filename, 'w', encoding='utf-8') as file:
        """
        return
        """
        return (file.write(text))
