#!/usr/bin/python3
""" Creating a user class """


from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, String, ForeignKey


class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship(
                'City', backref='state', cascade='all, delete, delete-orphan'
                )

    else:
        @property
        def cities(self):
            cities = models.storage.all(City)

            return [city for city in cities.values() if city.state_id == self.id]

