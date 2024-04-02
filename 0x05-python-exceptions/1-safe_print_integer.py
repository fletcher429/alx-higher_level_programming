#!/usr/bin/python3
def safe_print_integer(value):
    """
    Try to print the integer
    Returns true if the interger was printed correctly
    """
    try:
        print("{:d}".format(value))
        return True
    # Return false if the int was not printed correctly
    except:
        return False
