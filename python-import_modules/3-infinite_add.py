#!/usr/bin/python3
from sys import argv


def _infinite_add_():
    number = 0
    for i in argv[1:]:
        number += int(i)
    print("{}".format(number))


if __name__ == "__main__":
    _infinite_add_()
