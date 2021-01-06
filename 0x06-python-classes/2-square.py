#!/usr/bin/python3
"""Create class Square"""


class Square:
    """class that calculates the square with the size"""
    __size = 0

    def __init__(self, size=0):
        """Initializacion of the class Square

        Args:
            size is a int and is the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
