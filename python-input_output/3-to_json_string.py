#!/usr/bin/python3
"""
Module 3-to_json_string
returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    '''returns the JSON representation
    args:
        my_obj: object
        Return a object from JSON representation'''
    return json.dumps(my_obj)
