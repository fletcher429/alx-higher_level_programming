#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    w = add(a, b)
    x = sub(a, b)
    y = mul(a, b)
    z = div(a, b)

    print("{} + {} = {}".format(a, b, w))
    print("{} - {} = {}".format(a, b, x))
    print("{} * {} = {}".format(a, b, y))
    print("{} / {} = {}".format(a, b, z))
