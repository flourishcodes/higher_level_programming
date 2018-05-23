#!/usr/bin/python3
""" Class Base"""

import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiation of id for Base Class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method that returns the JSON string representation of function'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Method that writes JSON string representation to file'''
        with open("{}.json".format(cls.__name__), 'w') as f:
            new = []
            for i in list_objs:
                new.append(i.to_dictionary())
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        '''Method that retursn the list of JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''class method that prints instances'''
        temp = cls(1, 1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        '''Class Method that returns a list of instances'''
        new_list = []
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                new = cls.from_json_string(f.read())
        except IOError:
            return []

        for i in new:
            new_list.append(cls.create(**i))
        return new_list