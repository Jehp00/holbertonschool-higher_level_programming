#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = [0 for j in range(list_length)]
    for i in range(list_length):
        try:
            newList[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            newList[i] = 0
            print("division by 0")
        except TypeError:
            newList[i] = 0
            print("wrong type")
        except IndexError:
            newList[i] = 0
            print("out of range")
        finally:
            pass
    return newList
