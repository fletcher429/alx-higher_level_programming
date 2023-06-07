#!/usr/bin/python3
def uppercase(str):
    store = ""
    a = ord('a')
    z = ord('z')
    for char in str:
        if a <= ord(char) <= z:
            upper = chr(ord(char) - 32)
            store += upper
        else:
            store += char
    print("{}".format(store))
