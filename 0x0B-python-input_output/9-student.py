#!/usr/bin/python3
"""define a class student"""


class Student:
    """intilize the class with th attr"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """retrieve a dictionary represantation of a student"""

    def to_json(self):
        return vars(self)
