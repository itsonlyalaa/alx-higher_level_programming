#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for lt in reversed(my_list):
            print('{:d}'.format(lt))
