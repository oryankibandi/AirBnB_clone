#!/usr/bin/python3
"""cities module"""

from models.base_model import BaseModel


class City(BaseModel):
    """All cities listed"""
    state_id = ''
    name = ''
