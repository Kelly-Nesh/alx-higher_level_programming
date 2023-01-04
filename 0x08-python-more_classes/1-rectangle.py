#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """A rectangle representation."""
    def __init__(self, width=0, height=0):
        """Initialize rectangle properties.

        Args:
            width (int). The width of the rectangle
            height (int). The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the current rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the current rectangle
            depending on type and value
        """
        if not isinstance(width, (int)):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Get the height of the current rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the current rectangle
            depending on type and value
        """
        if not isinstance(height, (int)):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
