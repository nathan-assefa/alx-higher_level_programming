#!/usr/bin/python3
""" This script defines the satate object in the database
using ORM"""


if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    Base = declarative_base()
    class State(Base):
        """This class defines the methadata for the table 'states'"""

        __tablename__ = 'states'

        id = column(integer, primary_key=true, unique=true)
        name = column(string(30), nullable=false)
        

