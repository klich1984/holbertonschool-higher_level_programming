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
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter height"""
        self.__height = height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter x"""
        self.__x = x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter x"""
        self.__y = y
