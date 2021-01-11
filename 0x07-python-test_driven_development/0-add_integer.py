#!/usr/bin/python3
"""sums two integers"""


def add_integer(a, b=98):
    """Add two integers, of type float and integer

    Args:
        a (int, float): Integer or float
        b (int, float): Integer or float. Defaults to 98.

    Returns: the sum of two integers provided they are of type integer or float
    otherwise an exception with an error
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
