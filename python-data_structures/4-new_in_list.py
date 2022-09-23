#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)
    new_list = my_list.copy()
    for n in range(0, len(new_list)):
        if n == idx:
            new_list[n] = element
            return (new_list)