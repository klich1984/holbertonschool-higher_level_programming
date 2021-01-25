#!/usr/bin/python3
"""create class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle

    Args:
        Base (class): inherits the class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor the class Rectangle

        Args:
            width (int): [description]
            height (int): [description]
            x (int): [description]. Defaults to 0.
            y (int): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter width"""
        self.check_height_with(width, "width")
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter height"""
        self.check_height_with(height, "height")
        self.__height = height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter x"""
        self.check_x_y(x, "x")
        self.__x = x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter x"""
        self.check_x_y(y, "y")
        self.__y = y

    def check_height_with(self, value, name):
        """method check_height_with"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def check_x_y(self, value, name):
        """method check_ValueError"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """method area"""
        return self.__height * self.__width
