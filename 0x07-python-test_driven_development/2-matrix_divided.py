#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list):  list of lists of integers or floats
        div (int, float): is the number by which each element
        of the matrix will be divided, it must be different from 0
    Return: new matrix with numbers divided

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """
    if type(div) != int and type(div) != float:
                raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    #range(len(matrix)) es largo de filas = 2
    #range(len(matrix[f])) es el largo de columnas = 3

    new_matrix = []
    for f in range(len(matrix)):
        new_matrix.append([])
        for c in range(len(matrix[f])):
            if type(matrix[f][c]) != int and type(matrix[f][c]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[f].append(round(matrix[f][c]/div, 2))
    return new_matrix
