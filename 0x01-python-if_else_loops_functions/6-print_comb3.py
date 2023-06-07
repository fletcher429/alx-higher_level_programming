#!/usr/bin/python3
for n in range(0, 9):
    for m in range(n, 10):
        if n == m:
            continue
        print("{}{}".format(n, m), end=", " if not (n == 8 and m == 9) else "\n")
