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


    def area(self):
        '''public method to calculate the area'''
        area_square = self.__size ** 2
        return area_square
