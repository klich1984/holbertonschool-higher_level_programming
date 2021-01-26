#!/usr/bin/python3
"""create class Square that inherits from Rectangle"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle

    Args:
        Rectangle (class): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ creation constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ method __str__ """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width))
