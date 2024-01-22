#!/usr/bin/python3
"""a module to text indentation"""


def text_indentation(text):
    """a function that prints a text"""
    chars = [".", ":", "?"]

    if type(text) is not str:
        raise TypeError("text must be a string")

    lst = False
    for i in text:
        if i in chars:
            print(i)
            print()
            lst = True
        else:
            if lst is True and i == " ":
                lst = False
                continue
            else:
                print(i, end="")
                lst = False
