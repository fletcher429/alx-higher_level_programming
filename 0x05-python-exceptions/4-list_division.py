#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides elements in a list by 2
        Args:
            my_list_1: the first list
            my_lis_2: this is the second list
            list_length: the length of the list
    """
    try:
        for i in range(0, list_length):
            division = my_list_1[i] / my_list_2[i]
    except  ZeroDivisionError:
        print("division by 0")
        division = 0
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
       # a, b isinstance(int, float)

