#!/usr/bin/python3
"""
Module square
creating a class with one attribute Size
"""


class Square:
    '''
    class with attribute'''

    def __init__(self, size=0):
        '''attribute
        arguments:
            size: size of square'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        '''getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter for size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value


    def area(self):
        '''public method to calculate the area'''
        area_square = self.__size ** 2
        return area_square