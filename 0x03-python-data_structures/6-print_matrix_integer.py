#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix)-1:
        for f in range(len(matrix)):
            for c in range(len(matrix[f])-1):
                print("{:d} ".format(matrix[f][c]), end="")
            print("{:d}".format(matrix[f][c+1]))
    else:
        print()
