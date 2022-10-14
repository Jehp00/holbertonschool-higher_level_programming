#!/usr/bin/python3
"""
Module 11-student.
Creates a Student class.
"""


class Student:

    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of attributes
        Returns: the dict representation of the instance.
        """
        dictionary = dict()
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            for elem in attrs:
                if elem in self.__dict__:
                    dictionary.update({elem: self.__dict__[elem]})
            return dictionary
        return self.__dict__.copy()
