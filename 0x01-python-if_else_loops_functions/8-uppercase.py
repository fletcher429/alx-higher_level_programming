#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for char in (str):
        asci_val = ord(char)
        if 97 <= asci_val <= 122:
            char = chr(asci_val - 32)
        print("{}".format(char), end="")
    print()
