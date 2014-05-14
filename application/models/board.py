#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#import sys


class Board:
    """docstring for Board"""
    def __init__(self):
        return self

    def boardname():
        doc = "The boardName property."

        def fget(self):
            return self._boardName

        def fset(self, value):
            self._boardName = value
        return locals()
    boardName = property(**boardname())


    def boardfolder():
        doc = "The boardFolder property."

        def fget(self):
            return self._boardFolder

        def fset(self, value):
            self._boardFolder = value
        return locals()
    boardFolder = property(**boardfolder())
    
    def threads():
        doc = "The threads property."

        def fget(self):
            return self._threads

        def fset(self, value):
            self._threads = value
        return locals()
    threads = property(**threads())