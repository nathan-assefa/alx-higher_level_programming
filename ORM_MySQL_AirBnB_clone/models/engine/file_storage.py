#!/usr/bin/python3
""" This is the engine for flat file system """


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
import json


class FileStorage:
    """Backend design for flat file system"""

    __file_name = "file.json"
    __objects = {}

    __class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        # Add more class mappings as needed
    }

    def all(self, cls=None):
        objects = FileStorage.__objects
        if not cls:
            return objects

        return {key: obj for key, obj in objects.items() if cls == type(obj)}

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Writing into a json file"""
        with open(FileStorage.__file_name, "w", encoding="utf-8") as file:
            # First serilize the object using 'to_dict' method
            py_dict = {
                    key: val.to_dict()
                    for key, val in FileStorage.__objects.items()
                    }
            json.dump(py_dict, file, indent=2)


    def reload(self):
        """Reloading objects from json file"""
        try:
            with open(FileStorage.__file_name, encoding="utf-8") as file:
                py_dict = json.load(file)
        
            class_mapping = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                # Add more class mappings as needed
            }

            for obj in py_dict.values():
                class_name = obj["__class__"]
                if class_name in class_mapping:
                    cls = class_mapping[class_name]
                    self.new(cls(**obj))
                else:
                    raise ValueError
        except Exception:
            pass

    """
    def reload(self):
        try:
            with open(FileStorage.__file_name, encoding="utf-8") as file:
                py_dict = json.load(file)

            for obj in py_dict.values():
                class_name = obj["__class__"]
                if class_name in FileStorage.__class_mapping:
                    cls = FileStorage.__class_mapping[class_name]
                    self.new(cls(**obj))
                else:
                    raise ValueError(f"Unknown class name: {class_name}")
        except Exception:
            pass
        """

    def delete(self, obj=None):
        if obj:
            key = type(obj).__name__ + "." + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
