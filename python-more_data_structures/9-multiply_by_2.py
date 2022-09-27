#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    str = {}
    for i, j in a_dictionary.items():
        str[i] = a_dictionary[i] * 2
    return str
