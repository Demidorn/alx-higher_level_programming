#!/usr/bin/python3
""" Defines a rectangle"""


class Rectangle:
    """ defined by instance of height and width"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes rectangle instance
            Args:
            width = width of a rectangle
            heigth = heigth of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    def __str__(self):
        """ generates a string representation"""
        if self._height == 0 or self._width == 0:
            return ''
        rec_str = ''
        for i in range(self._height):
            for j in range(self._width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returns a string representation of the rectanglee by using eval() """
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Deletes the rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """calculates area of a rectangle instance by
        returning width * height """
        return self._width * self._height

    def perimeter(self):
        """calculates perimeter of a rectangle
        given by 2*(height + width """
        if self._height == 0 or self._width == 0:
            return 0
        return 2 * (self._width + self._height)
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area

        Args:
            rect_1 = rectangle instance
            rect_2: Rectangle instance different from rect_1

        Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
