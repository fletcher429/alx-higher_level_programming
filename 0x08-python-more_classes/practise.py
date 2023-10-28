x = 10  # Global variable

def outer():
    y = 5  # Enclosing (non-local) variable
    x = 20

    def inner():
        nonlocal y  # Declare 'y' as non-local
        y = 20  # Modifying the enclosing variable

    inner()
    print(y)  # Accessing the modified enclosing variable
    print(x)

outer()
print(x)  # Accessing the global variable
