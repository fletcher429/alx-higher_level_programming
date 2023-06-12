#!/usr/bin/python3
from test import add, mul, div, sub
from sys import argv
if __name__ == "__main__":
    result = 0
    a = int(argv[1])
    b = int(argv[3])
    oper = argv[2]
    for i in range(1, len(argv)):
        if oper == '+':
            result = add(a, b)
        elif oper == '-':
            result = sub(a, b)
        elif oper == '*':
            result = mul(a, b)
        elif oper == '/':
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    print("{} {} {} = {}".format(a, oper, b, result))