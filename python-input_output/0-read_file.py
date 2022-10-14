#!/usr/bin/python3
"""
Module 0-read_file
read a file text and print it
"""


def read_file(filename=""):
    '''read the file and print it
    args:
        filename: string or text to be read'''
    with open('my_file_0', encoding="utf-8") as file:
        read_data = f.read()
