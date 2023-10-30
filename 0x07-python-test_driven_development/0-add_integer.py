#!/usr/bin/python3
"""
Adds integers
    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """Adds integer version of a and b

    Args:
        a (int or float): number to be added
        b (int or float): number to be added
    """
    if not isinstance(a, int) and not isinstance(a, float):
        try:
            a = int(a)
        except TypeError:
            raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        try:
            b = int(b)
        except TypeError:
            raise TypeError('a must be an integer')

    return int(a) + int(b)
