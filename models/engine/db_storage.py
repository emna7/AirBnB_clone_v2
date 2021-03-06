#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
import os

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ This class maps python classes to SQL Database using SQLAlchemy
    Attributes:
        __engine: the engine used
        __objects: the session linking the db with program
    """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review", "Amenity"]

    def __init__(self):
        """ Init method for DBStorage class """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        dbname = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user,
                                   password,
                                   host,
                                   dbname), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of objects which their name is specified """
        mylist = list()
        newdict = dict()
        if cls is not None:
            obj = eval(cls)
            mylist = self.__session.query(obj).all()
            for item in mylist:
                key = item.__class__.__name__ + "." + item.id
                newdict[key] = item
        else:
            for obj in self.all_classes:
                obj = eval(obj)
                mylist = self.__session.query(obj).all()
                for item in mylist:
                    key = item.__class__.__name__ + "." + item.id
                    newdict[key] = item
        return (newdict)

    def new(self, obj):
        """ Adds a new object to the database """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes made in current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an existing object from the database """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in database and set a session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(expire_on_commit=False)
        session_factory.configure(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """a public method def close(self):: call remove() method on
        the private session attribute (self.__session) """
        self.reload()
        self.__session.close()
