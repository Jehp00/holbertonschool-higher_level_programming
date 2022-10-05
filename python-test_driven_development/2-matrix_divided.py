#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix by a number
"""


def matrix_divided(matrix, div):
    '''
    Returns a new matrix with the results
    of the division of matrix by div with 2 decimals'''

    new_matrix = [] 
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
        "of integers/floats")
    for r in matrix:
        if len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for y in r:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for r in matrix:
        len_rows.append(len(r))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise  ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in i] for i in matrix]

    return(new_matrix)
