#!/usr/bin/python3
"""
    function to divded elements in a matrix
"""
def matrix_divided(matrix, div):
    row_len = len(matrix[0])
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
            elif not all(len(row) == row_len for row in matrix):
                raise TypeError("Each row of the matrix must have the same size")
    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result
