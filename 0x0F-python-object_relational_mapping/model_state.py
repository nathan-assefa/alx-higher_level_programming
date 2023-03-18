#!/usr/bin/python3
""" This script defines the satate object in the database
using ORM"""


if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.orm import sessionmaker

    Base = declarative_base()
    class State(Base):
        __tablename__ = 'states'

        id = column(integer, primary_key=true, unique=true)
        name = column(string(30), nulable=false)
        

