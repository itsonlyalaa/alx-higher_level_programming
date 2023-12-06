#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for k in a_dictionary:
        new_dictionary[k] *= 2
    return new_dictionary
