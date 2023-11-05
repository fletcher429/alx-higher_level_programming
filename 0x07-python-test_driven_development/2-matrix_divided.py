#!/usr/bin/python3
""""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    len_row = len(matrix[0])
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # initilize a new matrix to store the results
    new_matrix = []

    # use a for loop to iterate through the row
    for row in matrix:
        # checks if each row is of the same size
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")

        # intilize a empty to store the elements in a row
        new_row = []
        # iterate through each element in a row
        for element in row:
            # divide each element by specified div
            result = element / div
            # round the result to 2dp
            result = round(result, 2)
            # In new row append result for each element
            new_row.append(result)
        # Append the rows to the em2-matrix_divided.py:28:80: E501 line too long (88 > 79 characters)ty matrix created
        new_matrix.append(new_row)
    # Return new matrix
    return new_matrix
