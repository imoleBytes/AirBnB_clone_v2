#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import models
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # cities = Column
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """returns cities with state_id = self.id"""
        all_objects = models.storage.all()
        lst_cities = []
        result = []
        for key in all_objects:
            ky = key.replace('.', ' ')
            clss = shlex.split(ky)
            if (clss[0] == 'City'):
                lst_cities.append(all_objects[key])
        for el in lst_cities:
            if (el.state_id == self.id):
                result.append(el)
        return result
