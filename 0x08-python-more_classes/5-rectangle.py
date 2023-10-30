#!/usr/bin/python3
""" Defines a rectangle"""


class Rectangle:
    """ defined by instance of height and width"""
    def __init__(self, width=0, height=0):
        """ initializes rectangle instance
            Args:
            width = width of a rectangle
            heigth = heigth of a rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ generates a string representation"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returns a string representation of the rectanglee by using eval() """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes the rectangle """
        print("Bye rectangle...")

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of a rectangle instance by
        returning width * height """
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of a rectangle
        given by 2*(height + width """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
