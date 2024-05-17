#!/usr/bin/python3


class DBStorage:
    __engine = None
    __session = None

    def close(self):
        """ call remove() method on the private session attribute
            (self.__session)
        """
        self.__session.remove()
