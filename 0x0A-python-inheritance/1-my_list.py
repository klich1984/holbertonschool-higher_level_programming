#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """Class MyList"""
# method

    def print_sorted(self):
        """method print list in ascending sort"""
        print(sorted(self))
