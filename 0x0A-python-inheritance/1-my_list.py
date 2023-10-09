#!/usr/bin/python3
"""
    Define a class that inherits from list as base
"""
class MyList(list):
    
    def print_sorted(self):
        sort_list = sorted(self)

        print(sort_list)



