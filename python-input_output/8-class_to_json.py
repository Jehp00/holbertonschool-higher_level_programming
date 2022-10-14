#!/usr/bin/python3
"""
Module 10-class_to_json.
Returns the dictionary description with
simple data structure for JSON serialization
of an object.
"""


def class_to_json(obj):
    """Creates a dict description of object.
    Args:
        obj: object to serialize
    Returns: dictionnary description
    """
    return obj.__dict__
