# 🐍 Python Errors and Exceptions 🚫

## Types of Errors in Python

### 1. Syntax Errors
Syntax errors occur when the code violates the syntax rules of Python, resulting in the interpreter being unable to execute the code.

Example:
```python
print("Hello World")  # Missing closing parenthesis
```

### 2. Exception Errors
Exception errors occur during the execution of the program when something unexpected happens.

Example:
```python
x = 10
y = 0
z = x / y  # Division by zero error
```

## Common Exceptions

### 1. `SyntaxError`
Occurs when the parser encounters a syntax error.

### 2. `NameError`
Occurs when a local or global name is not found.

### 3. `TypeError`
Occurs when an operation or function is applied to an object of an inappropriate type.

### 4. `ZeroDivisionError`
Occurs when division or modulo by zero is performed.

### 5. `IndexError`
Occurs when a sequence subscript is out of range.

### 6. `ValueError`
Occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value.

### 7. `KeyError`
Occurs when a dictionary key is not found.

### 8. `FileNotFoundError`
Occurs when a file or directory is requested but cannot be found.

## Handling Exceptions

```python
try:
    # Code block that may raise an exception
    result = x / y
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero!")
```
