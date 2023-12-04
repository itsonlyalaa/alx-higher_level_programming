#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + ('0', '0')
    b = tuple_b + ('0', '0')

    res1 = int(a[0]) + int(b[0])
    res2 = int(a[1]) + int(b[1])

    return res1, res2
