#!/usr/bin/python3
""" module of base class """


import json
import csv
import turtle


class Base():
    """ base class for checking other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of base class """
        if id is None:
            Base.__nb_objects += 1
            seld.id = Base.__nb_objects
        else:
            self.iid

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json str of list of dicts """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("argument must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of instances to file """
        if list_objs:
            lis = [obj.to_dictionary() for obj in list_objs]
            json_obj = cls.to_json_string(lis)
        else:
            json_obj = "[]"
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        """ from json string to list """
        if type(json_string) != str and json_string is not None:
            raise TypeError
        if json_string is None or json_string == "[]" or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create instance of all attributes set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ loads list of instances from file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                obj_list = f.read()
            new = []
            for obj in cls.from_json_string(obj_list):
                new.append(cls.create(**obj))
            return new
        except FileNotFoundError:
            return []

    @classmetthos
    def save_to_file_csv(cls, list_objs):
        """ serializes list of objects """
        if type(list_objs) != list:
            raise TypeError
        for obj in list_objs:
            if not isinstance(obj, cls):
                raise TypeError
        tls = [obj.to_dictionary() for obj in list_objs]
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            field_names = ['id', 'size', 'x', 'y']
        with open(file_name, mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fiels_names)
            for dic in tls:
                writer.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes list of objects """
        obj_list = []
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            field_names = ['id', 'size', 'x', 'y']
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                r_list = csv.DictReader(file, fieldnames=field_names)
                for row in r_list:
                    dic = {}
                    for key, value in dict(row).items():
                        dic[key] = int(value)
                    obj_list.append(cls.create(**dic))
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ print with turtle list of rectangles and squares """
        turtles1 = []
        turtles2 = []
        turtles3 = []
        turtles4 = []

        for i in range(len(list_rectangles) + len(list_squares) * 8):
            turtles1.append(turtle.Turtle())
            turtles2.append(turtle.Turtle())
            turtles3.append(turtle.Turtle())
            turtles4.append(turtle.Turtle())
        pos_x = 0
        pos_y = 0
        i = 0
        x_plan = 0
        y_plan = 0
        for obj in list_rectangles:
            i += 1
            dic = obj.to_dictionary()
            print(dic)
            w = dic['width']
            h = dic['height']
            x = dic['x']
            y = dic['y']
            plan_x = w + x + pos_x
            plan_y = h + y + pos_y
            max_x = max(plan_x, plan_y) + 20
            max_y = -max(plan_x, plan_y) - 20
            turtle.setworldcoordinates(-30, 30, max_x, max_y)
            turtles1[i].penup()
            turtles1[i].goto(pos_x, 0)
            turtles1[i].pendown()
            turtles1[i].forward(w + x + 10)
            turtles1[i].write(w)

            turtles2[i].penup()
            turtles2[i].goto(pos_x, 0)
            turtles2[i].pendown()
            turtles2[i].right(90)
            turtles2[i].forward(h + y + 10)
            turtles2[i].write(h)
            i += i

            turtles1[0].speed(1)
            turtles1[0].color('red')
            turtles1[0].pensize(1)

            turtles1[0].goto(pos_x, 0)
            turtles1[0].pendown()
            turtles1[0].goto(pos_x + x, -y)
            turtles1[0].begin_fill()
            turtles1[0].color('blue')
            turtles1[0].pensize(5)
            turtles1[0].forward(w)
            turtles1[0].right(90)
            turtles1[0].forward(h)
            turtles1[0].right(90)
            turtles1[0].forward(w)
            turtles1[0].right(90)
            turtles1[0].forward(h)
            turtles1[0].right(90)
            turtles1[0].end_fill()
            turtles1[0].penup()
            pos_x += w + 80

        old_plan_x = plan_x
        old_plan_y = plan_y
        pos_y += -150 - h
        pos_x = 0
        i = 0

        for obj in list_squares:
            i += 1
            dic = obj.to_dictionary()
            print(dic)
            s = dic['size']
            x = dic['x']
            y = dic['y']

            plan_x = s + x + pos_x + old_plan_x + 50
            plan_y = s + y + pos_y + old_plan_y + 50
            max_x = max(plan_x, plan_y) + 20

            turtles3[i].penup()
            turtles3[i].goto(pos_x, pos_y)
            turtles3[i].pendown()
            turtles3[i].forward(x + s + 10)
            turtles3[i].write(s)

            turtles4[i].penup()
            turtles4[i].goto(pos_x, pos_y)
            turtles4[i].pendown()
            turtles4[i].right(90)
            turtles4[i].forward(y + s + 10)
            turtles4[i].write(s)
            i += i

            turtles1[0].speed(1)
            turtles1[0].color('red')
            turtles1[0].pensize(1)

            turtles1[0].goto(pos_x, pos_y)

            turtles1[0].pendown()
            turtles1[0].goto(pos_x + x, pos_y - y)
            turtles1[0].begin_fill()
            turtles1[0].color('green')
            turtles1[0].pensize(5)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].end_fill()
            turtles1[0].penup()
            pos_x += s + 80
            turtle.setworldcoordinates(-30, 30, max_x, -max_x)
        turtle.Screen().exitonclick()
