#!/usr/bin/python3
""" create class Square that inherits from Rectangle """
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

    @property
    def size(self):
        """ method getter size """
        return self.width

    @size.setter
    def size(self, size):
        """ method setter size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
            """ method update """
            if len(args) > 4:
                l = 4
            else:
                l = len(args)
            atributs = ["id", "size", "x", "y"]
            if l > 0:
                for i in range(l):
                    # setattr(objeto, atributos, nuevo_valor)
                    setattr(self, atributs[i], args[i])
            else:
                # key toma el valor que le pasan y .items es el valor de la key
                for key, value in kwargs.items():
                    if hasattr(self, key) is True:
                        setattr(self, key, value)

    def to_dictionary(self):
            """ method to_dictionary """
            dic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
            return(dic)
