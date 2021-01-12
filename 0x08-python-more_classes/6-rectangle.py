#!/usr/bin/python3
"""create Module whit the Class Rectangle"""


class Rectangle:
    """ that defines a rectangle

    Raises:
        TypeError: when width is diferent be an integer
        ValueError: when width is less than 0
        TypeError: when height is diferent be an integer
        ValueError: when height is less than 0

    Returns:
        [type]: [description]
    """

    number_of_instances = 0

    # defino constructor
    def __init__(self, width=0, height=0):
        """Constructor for instance Rectangle

        Args:
            width (int): whidth of the rectangle. Defaults to 0.
            height (int): height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """getter for width

        Returns:
            [type]: [description]
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value (int): the width of the rectangle
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for width"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
            value (int): the height of the rectangle
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method area

        Returns:
            [int]: the rectangle area
        """

        return self.__width * self.__height

    def perimeter(self):
        """method perimeter

        Returns:
            [int]:  the rectangle perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.height * 2

    def __str__(self):
        """print the rectangle with the character #

        Returns:
            [str]: [description]
        """

        string = ""
        if self.width == 0 or self.height == 0:
            return string
        else:
            return "\n".join(["#" * self.__width] * self.height)

    def __repr__(self):
        """call __repr__ for print

        Returns:
            [str]: [description]
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """destructor of the object and Print Bye rectangle"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1
