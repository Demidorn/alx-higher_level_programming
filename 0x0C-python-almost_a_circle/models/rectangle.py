#!/usr/bin/python3
""" new class Rectangle that inherits
from Base class """


from models.base import Base


class Rectangle(Base):
    """ class representing rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ setting getter for width """
        return self.__width

    @proprty
    def height(self):
        """ setting getter for height """
        return self.__height

    @propert
    def x(self):
        """ getter for x """
        return self.__x

    @property
    def y(self):
        """ setting getter for y """
        return self.__y

    @width.setter
    def width(self, width):
        """ setter for width """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ setter for height """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ setter for x """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @x.setter
    def y(self, y):
        """ setter for y """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.__height * self.__width

    def display(self):
        """ prints reactangle with # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates rectangle instances """
        if args:
            x = 0
            for arg in args:
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                arg += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """  returns dict representation of the rectangle """
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['width'] = self.__width
        new_dict['height'] = self.__height
        new_dict['x'] = self.__x
        new_dict['y'] = self.__y
        return new_dict
