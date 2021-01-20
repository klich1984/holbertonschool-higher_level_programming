#!/usr/bin/python3
""" function that check if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of a_class

    Args:
        obj (object): [description]
        a_class (class): [description]
    Return: True in case exit o otherwise False
    """
    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False
