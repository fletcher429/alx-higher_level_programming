# /usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    ARGS - My_list[] where the items to printed are on
    x - number of elements in the list
    """
    succes_print = 0
    for i in range(x):
        """
        use exception to make sure the correct output is printed  
        """
        try:
            print("{}".format(my_list[i]), end="")
            succes_print += 1

        except IndexError:
            break
    print("")
    return succes_print
