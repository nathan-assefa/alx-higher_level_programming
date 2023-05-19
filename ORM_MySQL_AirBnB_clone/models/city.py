#!/usr/bin/python3
""" Creating a user class """


from models.base_model import BaseModel, Base
import models
from sqlalchemy import String, Column, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(
            String(60), ForeignKey('states.id', ondelete='CASCADE'), nullable=False
            )
