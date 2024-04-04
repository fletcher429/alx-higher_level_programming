# PYTHON TEST DRIVEN DEVELOPMENT

- Test driven development means writing your test before writing the actual _code_ - TDD

## THE DOCTEST

- The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

- A fucntion to add 2 digits

def add(a, b):
return a + b

- let us the write the test using docsting/doctest

"""
Add two integers
"""
def add(a, b)

> > > add (6 + 6)
> > > 12
> > > add(7, 8)
> > > 15
adding string and string

return (a + b)