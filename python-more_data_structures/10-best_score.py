#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    best_score = 0
    save = ['nothing']
    d = {}
    for i, j in a_dictionary.items():
        if j > best_score:
            best_score = j
            save[0] = i
    return save[0]
