#!/usr/bin/python3
"""This module initilize an object of class FileStorage"""
from models.engine.file_storage import FileStorage


# Creates variable storage of class FileStorage
storage = FileStorage()

# Reads json data and loads it into the system if available
try:
    storage.reload()
except FileNotFoundError:
    pass

