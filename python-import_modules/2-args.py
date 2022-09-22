#!/usr/bin/python3
from sys import argv


def _lenght():
    if len(argv) == 1:
        print("0 argument.")
    elif len(argv) == 2:
        print("1 aguments:\n1: {}".format(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    _lenght()
