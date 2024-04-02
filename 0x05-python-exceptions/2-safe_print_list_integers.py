#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Args:
    my_list - the list to printed
    x - is the number of items in the list
    success_print - keeps track of int that are printed sucessfully
    """
    succes_print = 0
    # A for loop to loop through all the items in the list
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            succes_print += 1
        except (TypeError, ValueError):
            continue
    print("")
    return succes_print