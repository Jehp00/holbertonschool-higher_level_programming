#!/usr/bin/python3
"""
Module 0-read_file
read a file text and print it
"""


def read_file(filename=""):
    '''read the file and print it
    args:
        filename: string or text to be read'''
    with read(filename) as f:
        for line in f:
            print(line, end="")
