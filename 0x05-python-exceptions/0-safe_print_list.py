# /usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Tries to print the interger in the List
    """
    succes_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            succes_print += 1
        except IndexError:
            break
    print("")
    return succes_print
