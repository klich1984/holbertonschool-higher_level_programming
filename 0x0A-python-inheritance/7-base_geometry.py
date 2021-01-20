#!/usr/bin/python3
"""Create class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value

        Args:
            name (str): name
            value (int): value a validate
        Return: Raise error
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
