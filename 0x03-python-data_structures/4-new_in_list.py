#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst = my_list[:]
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    else:
        lst[idx] = element
        return lst
