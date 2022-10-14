#!/usr/bin/python3
"""
Module 6-load_from_json_file
creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """Creates an object from filename.
    Args:
        - filename: name of the JSON file
    Returns: the object
    """
    with open(filename, 'r') as f:
        return json.load(f)
