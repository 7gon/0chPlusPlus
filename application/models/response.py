#!/usr/bin/python2.7


class Response:
    """docstring for Response"""
    def __init__(self):
        return self
    
    def message():
        doc = "The message property."

        def fget(self):
            return self._message

        def fset(self, value):
            self._message = value
        return locals()
    message = property(**message())

    def datetime():
        doc = "The datetime property."

        def fget(self):
            return self._datetime

        def fset(self, value):
            self._datetime = value
        return locals()
    datetime = property(**datetime())

    def resid():
        doc = "The resId property."

        def fget(self):
            return self._resId

        def fset(self, value):
            self._resId = value
        return locals()
    resId = property(**resid())

    def number():
        doc = "The number property."

        def fget(self):
            return self._number

        def fset(self, value):
            self._number = value
        return locals()
    number = property(**number())

    def session():
        doc = "The session property."

        def fget(self):
            return self._session

        def fset(self, value):
            self._session = value
        return locals()
    session = property(**session())

    def useragent():
        doc = "The userAgent property."

        def fget(self):
            return self._userAgent

        def fset(self, value):
            self._userAgent = value
        return locals()
    userAgent = property(**useragent())

    def remotehost():
        doc = "The remoteHost property."

        def fget(self):
            return self._remoteHost

        def fset(self, value):
            self._remoteHost = value
        return locals()
    remoteHost = property(**remotehost())