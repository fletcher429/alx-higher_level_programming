#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    num_len = len(argv)
    for arg in argv[1:]:
        num = int(arg)
        sum += num
    print("{:d}".format(sum))
