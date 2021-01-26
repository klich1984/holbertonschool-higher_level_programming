#!/usr/bin/python3
"""create class Base"""
import json


class Base():
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Creation constructor

        Args:
            id (int): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ method to_json_string """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
