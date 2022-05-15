#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128),  nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""
        @property
        def cities(self):
            """Devuelve la lista de instancias de Ciudad con
            state_id es igual al State.id actual"""
            cities = storage.all(City)      
            lista = []
            for valors in cities.values():
                if valors.state_id == self.id:
                    lista.append(valors)
            return lista