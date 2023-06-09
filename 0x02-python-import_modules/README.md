# Python Import and Modules

📚 **Imports** in Python allow you to access external modules and packages. They enhance code reusability and prevent duplication. 

🔹 **Importing Modules:** Use the `import` statement followed by the module name. Example: `import math` 

🔹 **Specific Imports:** Import specific functions or classes from a module. Example: `from math import sqrt, sin`

🔹 **Aliases:** Assign an alias to a module or function during import. Example: `import numpy as np`

📦 **Modules** in Python are files containing definitions, statements, and functions for reuse.

🔸 **Creating Modules:** Write code in a `.py` file, which becomes the module name. Example: `my_module.py`

🔸 **Using Modules:** Import modules and access their contents. Example: `import my_module`

🔸 **`__name__` Variable:** Helps differentiate between running a module directly or importing it.

``python
if __name__ == "__main__":
    # Code executed when the module is run directly
    pass
Import Examples:

    Importing an entire module:
## Import Examples

### Importing an entire module:

```python
import math

# Now you can use functions from the math module
print(math.sqrt(16))

# Importing specific functions from a module

```python
from math import sqrt, sin

# Now you can use sqrt() and sin() directly
print(sqrt(16))
print(sin(0.5))

