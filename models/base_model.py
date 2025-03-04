#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(
            String(60), primary_key=True, unique=True,
            nullable=False
            )
        created_at = Column(
            DateTime, default=datetime.utcnow(),
            nullable=False
            )
        updated_at = Column(
            DateTime, default=datetime.utcnow(),
            nullable=False
            )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for j, v in kwargs.items():
                if j == "created_at" or j == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if j != "__class__" and j != "_sa_instance_state":
                    setattr(self, j, v)
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
            if "id" not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))

    def delete(self):
        """Deletes an instance of the model"""
        from models import storage

        storage.delete(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in self.__dict__:
            del self.__dict__["_sa_instance_state"]
        return dictionary