#!/usr/bin/python3
""" Creating a user class """


from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, String, ForeignKey


class User(BaseModel, Base):
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    lase_name = Column(String(128), nullable=True)
