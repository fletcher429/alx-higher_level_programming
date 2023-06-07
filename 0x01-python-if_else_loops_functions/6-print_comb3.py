#!/usr/bin/python3
for n in range(0, 10):
    for m in range(n, 10):
        print(f"{n}{m:d}", end=", " if n < 9 else "\n")
    if n < 9:
        print("\b\b", end=", ")
