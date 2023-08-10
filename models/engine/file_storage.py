#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """
   This class manages storage of hbnb models in JSON format
   Using this way
   Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - will store all objects by <class name>.id

    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
   """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from models files"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

