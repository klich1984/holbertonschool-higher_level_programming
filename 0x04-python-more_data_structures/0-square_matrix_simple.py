#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [i[:] for i in matrix]
    for f in range(len(matrix)):
        for c in range(len(matrix[f])):
            new_matrix[f][c] = matrix[f][c]**2
    return new_matrix
