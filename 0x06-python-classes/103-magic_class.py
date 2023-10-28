#!/usr/bin/python3
""" Python class MagicClass that does exactly the same as
the given Python bytecode"""

import math


class MagicClass:
    """Magic class for given bytecode."""

    def __init__(self, radius=0):
        """constructor method
        Args:
            radius: (int): The radius of the new magicclass instance.
        """
        self.__radius = 0
        if not isintance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the class."""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """Returns the circumference of the class."""
        return (math.pi(2 * self.__radius))
