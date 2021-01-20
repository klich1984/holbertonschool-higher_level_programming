#!/usr/bin/python3
""" function that returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class
"""


def inherits_from(obj, a_class):
    """check if objt is an instance directly or indirectly)

    Args:
        obj (object): a object
        a_class (class): a class
    Return: True in case exit o otherwise False
    """

    if isinstance(type(obj), a_class) is False:
        return True
    else:
        return False
