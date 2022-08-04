#!/usr/bin/python3
"""class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances"""

import json


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
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

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
        from models.base_model import BaseModel
        
        classes = {"BaseModel": BaseModel}

        try:
            tmp = {}
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                tmp = json.load(f)
                for k, v in tmp.items():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            pass
