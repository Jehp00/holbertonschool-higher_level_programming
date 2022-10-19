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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height
    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x
    @property
    def x(self):
        '''gettter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y
    @property
    def y(self):
        '''getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Prints the rectangle in the terminal'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_string += '#'
            rect_string += '\n'
        print(rect_string[:-1])

    def __str__(self):
        '''method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return ("[Rectangle] ({}) {}/{} {}/{}".format(self.id, self.__x, self.__y,
                self.__width, self.__height))
