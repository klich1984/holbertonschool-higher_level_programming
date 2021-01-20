#!/usr/bin/python3
"""function that returns the list of available
    attributes and methods of an object:"""


def lookup(obj):
    """function that search attributes and methods

    Args:
        obj (obj): object that search attributes and methods
    """
    return (dir(obj))
