#!/usr/bin/python3
"""
Module 4-from_json_string
function that retunrs a object(python data structure)
 represented by a JSON string
"""


import json


def from_json_string(my_str):
    ''' Return the object represented my_str.
    Args:
        my_str: JSON string representation
    Returns: object'''
    return json.loads(my_str)