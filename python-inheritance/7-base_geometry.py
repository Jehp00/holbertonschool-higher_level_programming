#!/usr/bin/python3
"""
Module BaseGeometry
cretes a methood area but without
any parameter and have an integer validator
"""


class BaseGeometry:
    """BaseGeometry class that give a messege error
    where the method arrea is not implemented
    and checks for the value of integers"""
    def area(self):
        '''messege error by area()'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validator of the value of datas if are int
        args:
            name: string/variable to be check messege
            value: data to be check if is int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
