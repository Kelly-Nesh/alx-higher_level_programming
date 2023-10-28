#!/usr/bin/python3
"""function that adds 2 tuples.
Prototype: def add_tuple(tuple_a=(), tuple_b=()):
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """Returns a tuple with 2 integers"""
    taa = tba = tab = tbb = 0
    if len(tuple_a) == 1:
        taa = tuple_a[0]
    elif len(tuple_a) >= 2:
        taa = tuple_a[0]
        tab = tuple_a[1]
    if len(tuple_b) == 1:
        tba = tuple_b[0]
    elif len(tuple_b) >= 2:
        tba = tuple_b[0]
        tbb = tuple_b[1]
    a = taa + tba
    b = tab + tbb
    c = (a, b)
    return c
