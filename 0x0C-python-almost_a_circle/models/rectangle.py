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

    def display(self):
        """ method display task 5 """
        if int(self.__y) == 0:
            print("", end="")
        elif int(self.__y) == 1:
            print("")
        else:
            l = int(self.__y) - 1
            print("{}".format("\n" * l))
        # _ para eliminar advertencia de variable no usada
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ method __str__ """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ method update """
        if len(args) > 5:
            l = 5
        else:
            l = len(args)
        atributs = ["id", "width", "height", "x", "y"]
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
        dic = {"x": self.x, "y": self.y, "id": self.id,
               "height": self.height, "width": self.width}
        return(dic)
