#!/usr/bin/python
"""

"""

from models.base import Base
#Base = __import__('models/base').Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        pass

    # height
    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        pass

    # x
    @property
    def x(self):
        return self.__x

    @x.setter
    def width(self, value):
        pass

    # y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        pass