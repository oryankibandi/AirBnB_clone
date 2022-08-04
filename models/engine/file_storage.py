#!/usr/bin/python3
"""class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances"""

import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a
    JSON file and deserializes
    JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id"""
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for k, v in tmp.items():
                tmp[k] = v.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """deserializes the JSON file
        to __objects (only if the JSON
        file (__file_path) exists ;
        otherwise, do nothing. If the
        file doesn’t exist, no exception
        should be raised)"""
        
        classes = {"BaseModel": BaseModel}

        try:
            tmp = {}
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                tmp = json.load(f)
                for k in tmp:
                    self.__objects[k] = classes[tmp[k]["__class__"]](**tmp[k])
        except FileNotFoundError:
            pass
