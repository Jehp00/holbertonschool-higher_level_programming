#!/usr/bin/python3
"""
Module BaseGeometry
cretes a methood area but without
any parameter
"""


class BaseGeometry:
    """BaseGeometry class that give a messege error 
    where the method arrea is not implemented"""
    def area(self):
        '''messege error'''
        raise Exception("area() is not implemented")