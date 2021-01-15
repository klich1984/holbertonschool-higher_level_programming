#!/usr/bin/python3
"""Function that print name and last name"""


def say_my_name(first_name, last_name=""):
    """Print name and last name

    Args:
        first_name (str): string what contain teh name
        last_name (str): string what contain the last name. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
