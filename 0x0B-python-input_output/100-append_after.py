#!/usr/bin/python3
"""
import os module
"""
import os


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after lines containing search_string.
    """
    lines_to_append = []
    """
        use open to read and close file safely
    """

    with open(filename, "r") as file:
        """
        use the readline function
        """
        lines = file.readlines()

    with open(filename, "w") as file:
        """
        implement the open function
        """
        for line in lines:
            """ "
            write to the function
            """
            file.write(line)
            if search_string in line:
                file.write(new_string)
