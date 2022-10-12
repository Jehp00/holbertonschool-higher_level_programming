#!/usr/bin/python3
"""
Module inherits_from
checks if obj is in a specified class
directly or indirectly
"""
def inherits_from(obj, a_class):
    '''Returns True if is in class, False otherwise'''
    return issubclass(obj, a_class)
