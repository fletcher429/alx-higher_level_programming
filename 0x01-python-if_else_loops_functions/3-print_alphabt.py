#!/usr/bin/python3
for asci in range(ord('a'), ord('z') + 1):
    if asci == 113 or asci == 101:
        continue
    print("{}".format(chr(asci)), end="")
