#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for value in range(len(i)):
            if value < (len(i) - 1):
                print("{:d} ".format(i[value]), end="")
            else:
                print("{:d}".format(i[value]), end="")
        print("")
