#!/usr/bin/python3
"""Create class Square"""


class Square:
    """class that calculates the square with the size"""
    __size = 0

    def __init__(self, size=None):
        """Initializacion of the class Square

        Args:
            size is a int and is the size of the square
        """
        self.__size = size
