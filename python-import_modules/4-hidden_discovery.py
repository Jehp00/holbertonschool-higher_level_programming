#!/usr/bin/python3
import hidden_4


def _hidden():
    for i in dir(hidden_4):
        if i[:2] != "__":
            print("{}".format(i))


if __name__ == "__main__":
    _hidden()
