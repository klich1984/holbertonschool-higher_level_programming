#!/usr/bin/python3
"""function that returns an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """method that return an objet (python data struct)

    Args:
        my_str (str): file that convert a json python
    """
    js = json.loads(my_str)
    return js
