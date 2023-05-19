#!/usr/bin/python3
"""The driving power of relational databses"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage():
    """ This class comprises the ORM methods that helps us
    to interact with our detabase """

    __classNames = [
            State,
            City
            ]

    __engine = None
    __session = None

    def __init__(self):
        """ This is how we get conneted to the database.
        The four environmental variables are used for
        robust security """

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        query = self.__session.query(cls) if cls else self.__session.query(*DBStorage.__classNames)

        return {f"{type(obj).__name__}.{obj.id}": obj for obj in query}
        """
        #query to fetch all objects related to cls if cls
        #is not None. Otherwise fetch all
        list_obj = []
        if not cls:
           for obj in DBStorage.__classNames:
               list_obj += (self.__session.query(obj))
        else:
            list_obj = self.__session.query(cls)

        #return the dictionary reperesentation
        #return {v.__class__.__name__ + '.' + v.id: v for v in list_obj
        return {type(v).__name__ + '.' + v.id: v for v in list_obj}
        """
        """
        obj_dict = {}

        if cls:
            obj_dict.update(self.__session.query(cls))
        else:
            for key in DBStorage.__classNames:
                for row in self.__session.query(key):
                    obj_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return obj_dict
        """

    def new(self, obj):
        """ Adding the obj to the database """
        self.__session.add(obj)

    def save(self):
        """ commiting all changes to a database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete a session object if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ To Create all the tables on the database """
        from sqlalchemy.orm import sessionmaker
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
