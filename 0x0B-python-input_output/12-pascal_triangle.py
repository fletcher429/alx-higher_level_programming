#!/usr/bin/python3
"""returns a list of lists of int representing the Pascal's triangle of n"""


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
    if i > 0:
        prev_row = triangle[-1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
    triangle.append(row)
    return triangle
