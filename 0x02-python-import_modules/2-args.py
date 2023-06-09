#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    le = len(argv) - 1
    if le == 0:
        print(f"{le} arguments.")
    elif le == 1:
        print(f"{le} argument:")
    else:
        print(f"{le} arguments:")
    for i in range(1, le + 1):
        print(f"{i}: {argv[i]}")
