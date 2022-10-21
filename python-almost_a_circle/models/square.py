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
        super().__init__(size, size, x, y, id)
        self.update()

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
        return self.width

    @size.setter
    def size(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        '''updating attributes with args and kwargs'''
        if args:
            self = self.__dict__
            try:
                c = 0
                for i in self.keys():
                    if i == "Rectangle_height":
                        continue
                    self[i] = args[c]
                    c += 1
            except IndexError:
                c -= 1
        if kwargs:
            if not args:
                for k, v in kwargs.items():
                    setattr(self, k, v)