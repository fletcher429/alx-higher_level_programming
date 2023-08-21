#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    max_value = my_list[0]

    for ints in my_list:
        if ints > max_value:
            max_value = ints
    return max_value
