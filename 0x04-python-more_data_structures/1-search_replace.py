#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for items in my_list:
        if items == search:
            new_list.append(replace)
        else:
            new_list.append(items)
    return new_list
