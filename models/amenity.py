#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherit from the BaseModel class"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""