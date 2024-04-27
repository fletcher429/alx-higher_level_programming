# *ARGS AND **KWARGS

"""
    What is *args and **kwargs - they act like variadic function is C
    They take more than one argument
    Allows you to pass variable number of arguments to a function

"""
"""
test_var_args:
    Args: 
        f_args - this is justv a normal argument
        *argv - used actually to get variable number of agruments
        they are stored in a tuple 
        and can be accessed
"""
def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)

    for arg in argv:
        print ("another arg through *argv: ", arg)
# note that the yassob is the first argument
# all the remaining ill be accumulated in the args argument
test_var_args('yasoob', 'python', 'eggs', 'test')

# KWARGS - KEY WORD ARGUMENT
"""
It allows you to accept a variable number of keyword arguments
What are keyword arguments? - these are arguments passed to a function with key-value
syntax where they specifies the argument name and the value in the actual data

"""

