#!/usr/bin/python3
for num in range(25, -1, -1):
    if num % 2 == 0:
        print("{0}".format(chr(num % 26 + 65)), end="")
    else:
        print("{0}".format(chr(num % 26 + 97)), end="")
