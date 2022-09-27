#!/usr/bin/python3
def roman_to_int(roman_string):
    n_rom = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    value = 0
    num = 0
    len_num = roman_string
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for num in range(num, len(len_num)):
        if num < len(len_num) - 1 and n_rom[len_num[num]] < n_rom[len_num[num + 1]]:
            value -= n_rom[len_num[num]]
        else:
            value += n_rom[len_num[num]]
    return value
