#!/usr/bin/python3
"""module with a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """function that finds the biggest integer of a list."""
    if not my_list:
        return
    my_list.sort()
    return my_list[-1]
