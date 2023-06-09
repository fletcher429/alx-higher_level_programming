#!usr/bin/python3
from calculator_1 import sub, mul, div, add

a = 10
b = 5

add_res = add(a, b)
sub_res = sub(a, b)
mul_res = mul(a, b)
div_res = div(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add_res))
    print("{} - {} = {}".format(a, b, sub_res))
    print("{} * {} = {}".format(a, b, mul_res))
    print("{} / {} = {}".format(a, b, div_res))
