#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    str = {}
    sort = sorted(a_dictionary)
    for i in sort:
        str[i] = a_dictionary[i]
    for j, h in str.items():
        print(f"{j}: {h}")