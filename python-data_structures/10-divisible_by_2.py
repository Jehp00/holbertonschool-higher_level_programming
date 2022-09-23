#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Is_boolean = []
    for i in my_list:
        if i % 2 == 0:
            Is_boolean.append(True)
        else:
            Is_boolean.append(False)
    return (Is_boolean)
