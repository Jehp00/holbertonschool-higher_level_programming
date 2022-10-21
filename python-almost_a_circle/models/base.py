#!/usr/bin/python3
"""
Module base
creates a Base class for the pakage python
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Retunrs a list od dictionaries to JSON strings
        Args:
            list_objs: list of instances who inherits of Base
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation
        of list_objs to a file
        args:
            cls: class objet
            list_objs: list of instances who inherits of Base
        '''
        if list_objs is None or list_objs == []:
            Jsstr = "[]"
        else:
            Jsstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            f.write(Jsstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            - json_string: string to convert to list
        """
        str_lis = []
        if json_string is None or json_string == '':
            if type(json_string) is not str:
                raise TypeError("json_string must be a string")
            str_lis = json.load(json_string)
        return str_lis
