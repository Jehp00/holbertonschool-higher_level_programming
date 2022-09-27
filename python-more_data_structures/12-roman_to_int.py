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
    n = 0
    len_n = roman_string
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for n in range(n, len(len_n)):
        if n < len(len_n) - 1 and n_rom[len_n[n]] < n_rom[len_n[n + 1]]:
            value -= n_rom[len_n[n]]
        else:
            value += n_rom[len_n[n]]
    return value
