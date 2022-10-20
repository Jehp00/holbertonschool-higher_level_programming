#!/usr/bin/python3
"""
Module square
creates a Square
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)
    def __str__(self):
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return s