#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            n_matrix[i][j] = matrix[i][j] ** 2
    return n_matrix
