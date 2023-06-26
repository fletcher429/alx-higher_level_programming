# alx-higher_level_programming
## 0x05-python-exceptions

This repository contains Python scripts that demonstrate the use of exception handling to handle errors and exceptions in Python programming. Each file focuses on a specific task and showcases different aspects of exception handling.

📂 **Files**:

1. **0-safe_print_list.py**: This script implements the `safe_print_list` function, which prints a specified number of elements from a list. It handles potential errors, such as accessing elements beyond the list's length, using try-except blocks. The function returns the actual number of elements printed.

2. **1-safe_print_integer.py**: The `safe_print_integer` script defines a function that takes a value as input and prints it if it is an integer. It uses exception handling to catch non-integer values and returns `True` if the value is successfully printed as an integer. Otherwise, it returns `False`.

3. **2-safe_print_list_integers.py**: The `safe_print_list_integers` script implements a function that prints the first `x` elements of a list, but only if they are integers. Non-integer values are skipped silently. The script uses exception handling to prevent accessing elements beyond the list's length.

4. **3-safe_print_division.py**: This script contains the `safe_print_division` function, which divides two integers, prints the result, and returns the division value. It uses try-except-finally blocks to handle potential errors, including division by zero. The result is printed in the `finally` block to ensure it is always displayed, regardless of any exceptions that occur.

5. **4-list_division.py**: The `list_division` script defines a function that performs element-wise division of two lists. It returns a new list containing the division results. The script handles various exceptions, such as division by zero, wrong types, and accessing elements beyond the list's length, using try-except blocks.

6. **5-raise_exception.py**: The `raise_exception` script demonstrates how to manually raise a type exception without importing any modules. It defines a function that raises a type exception, and it can be used to understand the process of raising exceptions in Python.

7. **6-raise_exception_msg.py**: The `raise_exception_msg` script showcases how to raise a name exception with a custom message. It defines a function that raises a name exception and includes a user-defined message. This script provides insights into raising exceptions with custom messages without relying on imported modules.

📝 These scripts provide practical examples of exception handling in Python. Refer to each file for a more detailed explanation and the implementation of the respective tasks. 🚀