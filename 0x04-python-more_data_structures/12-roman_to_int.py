#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    res = 0
    items = 0
    roman = roman_string
    if type(roman) is not str or len(roman) == 0:
        return 0
    for items in range(items, len(roman)):
        if items < len(roman) - 1\
                and\
                roman_dict[roman[items]] <\
                roman_dict[roman[items + 1]]:
            res -= roman_dict[roman[items]]
        else:
            res += roman_dict[roman[items]]
        return res
