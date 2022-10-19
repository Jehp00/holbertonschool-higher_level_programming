#!/usr/bin/python3
"""
Module rectangle
"""


from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherited from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization asiigns the attributres of a rectangle
        args:
            width: width of the rectangle
            height: height of rectangle
            x: position in x
            y: position in y'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # width
    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter'''
        self.__width = value

    # height
    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        self.__height = value

    # x
    @property
    def x(self):
        '''gettter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter'''
        self.__x = value

    # y
    @property
    def y(self):
        '''getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter'''
        self.__y = value
