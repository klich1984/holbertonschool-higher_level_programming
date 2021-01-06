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
        self.__size = size

    def area(self):
        """Calculate the area

        Returns: that returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Properties getters of size
        Return: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter of size
        Args:
            size is a int and is the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value
