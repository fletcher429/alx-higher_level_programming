#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        n_row = []
        for num in row:
            n_row.append(num ** 2)
            new_matrix.append(n_row)
    return new_matrix
