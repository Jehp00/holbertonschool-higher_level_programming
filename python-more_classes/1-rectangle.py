#!/usr/bin/python3
"""
Module Rectangule
Creates a class rectangle
"""


class Rectangle:
    '''
    Rectangle class created by width and height'''

    def __init__(self, width=0, height=0):
        '''
        Initializes a Rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Returns the width of Rectangle instance'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Returns the height of Rectangle instance'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the width of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value