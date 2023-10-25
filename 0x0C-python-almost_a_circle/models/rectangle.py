#!/usr/bin/python3
"""
    import the Base module
"""
from .base import Base

"""
    define a class named Rectangle
"""


class Rectangle(Base):
    """
    init the class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        inherits from the base class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
        use the getter proptery to get the attributes of the class - width
    """

    @property
    def width(self):
        return self.__width

    """
        use the setter property to manipulates the width attribute
    """

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        self.__width = value

    """
         use the getter proptery to get the attributes of the class - height
    """

    @property
    def height(self):
        return self.__height

    """
         use the setter property to manipulates the height attribute
    """

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an int")

    """
        use the getter proptery to get the attributes of the class - x
    """

    @property
    def x(self):
        return self.__x

    """
         use the setter property to manipulates the x attribute
    """

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be greater than or equals to 0")
        self.__x = value

    """
        use the getter property to get the y attribute
    """

    @property
    def y(
        self,
    ):
        return self.__y

    """
        use the setter attribute to set the attributes of the y attribute
    """

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be greater than or equals to 0")
        self.__y = value
