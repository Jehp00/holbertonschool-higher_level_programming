#!/usr/bin/python3
"""
Module is_kind_of_class
checks if an attribute is in a class
or inherited class
"""


def is_kind_of_class(obj, a_class):
    '''return True if is in class, False otherwise'''
    return isinstance(obj, a_class)