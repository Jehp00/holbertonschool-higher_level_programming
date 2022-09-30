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
        self.__size = size

    @property
    def size(self):
        '''Return current size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set the size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''current square area'''
        return self.__size ** 2

    def my_print(self):
        '''Prints to stdout the square with #'''
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
