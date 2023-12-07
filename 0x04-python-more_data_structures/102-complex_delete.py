#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newList = []
    for k, v in a_dictionary.items():
        if value is v:
            newList.append(k)
    if len(newList) > 0:
        for new in newList:
            del a_dictionary[new]
    return a_dictionary
