#!/usr/bin/python3
"""
Module square
creates a Square
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherited from Rectangule with the same methods
    """
    def __init__(self, size, x=0, y=0, id=None):
        '''
        initialization of Square base rectangle
        args:
            id: id of square
            size: width and height of square
            x: position of square in eje x
            y: position of square in eje y
        '''
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        return [Square] (<id>) <x>/<y> - <size>
        size in our case is width public
        instance from Rectangle
        '''
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        '''getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__width = value
        self.__height = value
