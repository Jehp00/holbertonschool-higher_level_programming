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
        '''Prints the rectangle in the terminal
        with a given position'''
        if self.__width == 0 or self.__height == 0:
            return ""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''method so that it returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>'''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    """def update(self, *args):
        '''updating attributes with args'''
        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

        if len(args) == 4:
            self.id = args[0]
            self.__width = args[1] #In case of the lenght is gratter than expedted ailed
            self.__height = args[2]
            self.__x = args[3]

        if len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]

        if len(args) == 2:
            self.id = args[0]
            self.__width = args[1]

        if len(args) == 1:
            self.id = args[0]"""

                                    # better way
    """ c = 0
        self = self.__dict__
        try:
            for i in self.keys():
                self[i] = args[c]
                c += 1
        except IndexError:
            c = c - 1"""

    def update(self, *args, **kwargs):
        '''updating attributes with args and kwargs'''
        if args:
            c = 0
            try:
                for i in self.keys():
                    self[i] = args[c]
                    c += 1
            except IndexError:
                c = c - 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                
                if k == "width":
                    self.width = v

                if k == "height":
                    self.height = v


                if k == "y":
                    self.y = v

                if k == "x":
                    self.x = v
