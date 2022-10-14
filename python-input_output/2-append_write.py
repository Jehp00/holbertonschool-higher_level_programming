#!/usr/bin/python3
"""
Module 3-write_file.
Append in a text file.
"""


def append_write(filename="", text=""):
    '''Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: the new string added written'''
    with open(filename, 'a+') as file:
        return file.write(text)
