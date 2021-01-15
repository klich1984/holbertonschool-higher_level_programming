#!/usr/bin/python3
"""Function that prints a square whith the character #"""


def print_square(size):
    """Print square that size length of the variale size

    Args:
        size (int): size is the size length of the square
    """
    if type(size) is not int:
        if type(size) is float:
            if size < 0:
                raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for Row in range(size):
        for col in range(size):
            print("#", end="")
        print("")
