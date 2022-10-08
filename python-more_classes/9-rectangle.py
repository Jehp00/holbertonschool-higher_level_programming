#!/usr/bin/python3
"""
Module Rectangule
Creates a class rectangle
"""


class Rectangle:
    '''
    Rectangle class created by width and height'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Initializes a Rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''prints a representation of a
        rectangle instance, filled with {#}'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_string += str(self.print_symbol)
            rect_string += '\n'
        return rect_string[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Deletes a rectangle instance'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculates the area
        Returns the area of Rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculates the perimeter
        Returns the perimeter of Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size
        Args:
            size: size to set the new rectangle to
        Returns The new Rectangle instance
        """
        return cls(size, size)
