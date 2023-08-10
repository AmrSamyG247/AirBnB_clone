#!/usr/bin/python3
""" Review module for the HBNB project """
# Imports the Base Model Class
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class Attributes to store information """
    place_id = ""
    user_id = ""
    text = ""

