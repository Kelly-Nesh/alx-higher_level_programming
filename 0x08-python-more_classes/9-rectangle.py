#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """A rectangle class representation.

        Attributes:
            number_of_instances (int): Number of Rectangle instances available.
            print_symbol (str): Symbol for representing the Rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle properties.

        Args:
            width (int). The width of the rectangle.
            height (int). The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                rectangle.append(self.print_symbol)
            if i != self.__height - 1:
                rectangle.append("\n")
        try:
            return ("".join(rectangle))

        except TypeError:
            rect = ''
            for lst in rectangle:
                if lst == '\n':
                    rect += lst
                    continue
                rect += '['
                for itm in lst:
                    rect += "'" + itm + "'"
                    if itm != lst[-1]:
                        rect += ", "
                rect += ']'
            return rect

    def __repr__(self):
        """Returns string representation of the rectangle."""
        rep = "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
        return rep

    def __del__(self):
        """Print goodbye message on instance deletion."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns bigger rectangle instance."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)
