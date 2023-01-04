#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """A rectangle class representation."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle properties.

        Args:
            width (int). The width of the rectangle.
            height (int). The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or Set the width of the current rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the current rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int)):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Returns rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter."""
        if self.__width == 0 and self.__height == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns string representation of the rectangle."""
        rep = "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
        return (rep)
