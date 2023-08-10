#!/usr/bin/python3
"""This module defines a class User"""
# Imports the Base Model Class
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user Attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

