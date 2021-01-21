#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """method that create object from a JSON file

    Args:
        filename ([str]): file where load the json
    """
    with open(filename, encoding='utf-8') as f:
        js = json.load(f)
        return js
