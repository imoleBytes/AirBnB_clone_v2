#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from models.base_model import Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """DBStorage class definition"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)        

    def close(self):
        """ call remove() method on the private session attribute
            (self.__session)
        """
        self.__session.remove()
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in database"""
        
        dic = {}
        if cls:
            query = self.__session.query(cls)
            for i in query:
                ky = f"{cls.__name__}.{i.id}"
                dic[ky] = i
        else:
            all_cls = [State, City, User, Place, Review, Amenity]
            for clss in all_cls:
                query_ = self.__session.query(clss)
                for c in query_:
                    ky = f"{clss.__name__}.{c.id}"
                    dic[ky] = c
        return dic

    def reload(self):
        """reload data from database"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
