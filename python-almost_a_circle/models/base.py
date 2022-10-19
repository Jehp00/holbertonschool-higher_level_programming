#!/usr/bin/python3
"""
Module base
creates a Base class for the pakage python
"""


class Base:
    """Class with private attribute and init method
    with the public ittribute id"""
    __nb_objects = 0
    def __init__(self, id=None):
        '''Method that assigne a value to the arg id and count the number of obj
        args:
            id: id to asigne value'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
