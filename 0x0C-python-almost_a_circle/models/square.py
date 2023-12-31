#!/usr/bin/python3
""" square class """


from models.rectangle import Rectangle


class Square:
    """ class square that inherits from rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization of instances """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def __str(self):
        """ prints string instance of square """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ update square attributes """
        if args:
            x = 0
            for arg in args:
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.arg = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of Square"""
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
