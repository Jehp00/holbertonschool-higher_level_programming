#!/usr/bin/python3
"""
Module 1-my_list.
creates a class inheriting 
from the list class
"""


class MyList(list):
    '''
    MyList class inherited from
    list with nums unsirted'''
    def print_sorted(self):
    '''
    Public instance method that prints
    the new list'''
        new_list = self[:]
        new_list.sort()
        print(new_list)
