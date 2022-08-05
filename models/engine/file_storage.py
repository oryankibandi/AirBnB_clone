#!/usr/bin/python3
import json
from os import path
"""
This module contains the storage engine
"""

class FileStorage:
    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = {}     
        
    def all(self):
        """
        returns the __objects dictionary
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object
        """
        self.__objects[obj__class__.__name__.id] = obj
        
    def save(self):
        """
        serializes __objects to the JSON file 
        """
        ser_json = jsom.dumps(self.__objects)
        with open(self.__file_path), 'w') as f:
            f.write(ser_json)
            
            
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if path.exists(self.__file_path):
            with open(self.__file_path) as file:
                data = file.read()
                self.__objects = json.loads(data)
        else:   
            pass
