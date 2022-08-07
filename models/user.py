#!/usr/bin/python3
""" class User inheriting
from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class user, a subclass of BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
