#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""
This class contains the serialization models of the console
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        initializes the public instance attributes and methods
        Args:
            kwargs: key value pair with the parameters to initialize
        """

        if (len(kwargs)) != 0:
            for key, value in kwargs:
                if key is not '__class__':
                    self.key[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = created_at
            storage.new()

    def __str__(self):
        """
        prints a formated string with cass name and id
        """
        print("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary wwith keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
