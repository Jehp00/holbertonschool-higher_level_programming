#!/usr/bin/python3
"""
class with one attribute
"""


class Square:
    """
    class with attribute"""
    def __init__(self, size=0):
        """attribute
    args:
        size: size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
