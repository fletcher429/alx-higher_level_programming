#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print(f"{0}{n:d}", end=", ")
    else:
        print("{}".format(n), end=", "if n < 99 else "\n")
