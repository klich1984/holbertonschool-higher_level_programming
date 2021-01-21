#!/usr/bin/python3
""" function that returns the JSON representation
of an object (string)
"""
import json


def to_json_string(my_obj):
    """method that returns the JSON of a object.

    Args:
        my_obj (obj): string
    Return: returns the JSON representation of an object
    """
    return json.dumps(my_obj)
