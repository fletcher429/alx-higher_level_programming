#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    # Iterate over the list and add each unique integer to the set
    for num in my_list:
        unique_set.add(num)

    # Calculate the sum of the unique integers
    sum_unique = sum(unique_set)

    # Return the sum
    return sum_unique
