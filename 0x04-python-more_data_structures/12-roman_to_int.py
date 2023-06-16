#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    last = 0

    for numeral in roman_string[::-1]:
        if numeral not in lookup:
            return 0

        if lookup[numeral] < last:
            num -= lookup[numeral]
        else:
            num += lookup[numeral]

        last = lookup[numeral]

    return num
