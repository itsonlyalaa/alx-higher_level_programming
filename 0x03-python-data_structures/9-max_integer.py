#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    largeNum = my_list[0]
    for num in my_list:
        if num > largeNum:
            largeNum = num
    return largeNum
