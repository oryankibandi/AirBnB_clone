#!/usr/bin/python3
"""The reviews model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews"""
    place_id = ''
    user_id = ''
    text = ''
