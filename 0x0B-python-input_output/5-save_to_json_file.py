#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """method that write an Object to a text file

    Args:
        my_obj (obj): Object a writen
        filename (str): name of text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
