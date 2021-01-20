#!/usr/bin/python3
""" function that returns True if the object
    is exactly an instance of the specified
    class ; otherwise False."""

def is_same_class(obj, a_class):
    """method is_same_class

        Args:
            obj (object): The object
            a_class (class): [description]
        Returns: True if the object is exactly
        an instance of the specified class ; otherwise False
    """

    return type(obj) == a_class
