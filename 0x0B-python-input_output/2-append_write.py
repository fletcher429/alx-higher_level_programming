#!/usr/bin/python3
"""
    write a function that append to a file and returns number of characters
    written
"""
def append_write(filename="", text=""):
    """
        Using with  to open and safely closing the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """
            Define a var that redas the file
        """
        data = f.write(f"{text}")
    """
        Returns the number of characters written
    """
    return data