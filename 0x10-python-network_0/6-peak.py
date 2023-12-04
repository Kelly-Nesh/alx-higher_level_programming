#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers.
    Args:
        list_of_integers: (list) list of integers
    """
    if not list_of_integers:
        return
    list_of_integers.sort()
    return list_of_integers[-1]
