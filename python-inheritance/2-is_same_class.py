#!/usr/bin/python3
"""
Module is_same_class
checks if an attribute is in a class
"""
def is_same_class(obj, a_class):
    '''returns True or False if is not the same class
    Args:
        obj: attribute to compares
        a_class: class to check
    '''
    return type(obj) is a_class
