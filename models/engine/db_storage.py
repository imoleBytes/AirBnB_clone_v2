#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""


class DBStorage:
    """DBStorage class definition"""
    __engine = None
    __session = None

    def close(self):
        """ call remove() method on the private session attribute
            (self.__session)
        """
        self.__session.remove()
