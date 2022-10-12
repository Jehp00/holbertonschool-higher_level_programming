#!/usr/bin/python3
"""
Module MyList
takes a unsorted list and sorted
the numbers of the list
"""


class MyList(list):
    '''
    MyList class inheited from
    list with nums unsirted'''
    def print_sorted(self):
    '''
    Public instance method that prints
    the new list'''
        new_list = self[:]
        new_list.sort()
        print(new_list)
