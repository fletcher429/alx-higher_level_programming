#!/usr/bin/python3
for n in range(0, 10):
    for m in range(n, 10):
        print("{}{:d}".format(n, m), end=", " if n < 9 else "\n")
    if n < 9:
        end =", "
