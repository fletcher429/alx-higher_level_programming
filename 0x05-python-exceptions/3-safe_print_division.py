#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two int and return the results
        Args:
            a:
                The first integer
            b:
                the Second interger
    """
    div = 0
    try:
        div = a / b
    except (TypeError,ZeroDivisionError):
        div  = None
    finally:
        print("Inside result: {}".format(div))
    return (div)

