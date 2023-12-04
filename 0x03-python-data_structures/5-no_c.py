#!/usr/bin/python3
def no_c(my_string):
    newStr = ''
    for x in my_string:
        if x != 'C' and x != 'c':
            newStr += x

    return newStr
