#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="save-update, delete")

    @property
    def cities(self):
        """ Getter attribute that returns a dictionary of cities in a state """
        objects = storage.all(City)
        newdict = dict()
        for key, value in objects:
            from models import storage
            if value.id == self.id:
                newdict[key] = value
        return (newdict)
