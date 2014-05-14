#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


class Thread:
    """docstring for Thread"""
    def __init__(self, key):
        self.threadKey = key
        self.readsetting()

    def threadname():
        doc = "The threadName property."

        def fget(self):
            return self._threadName

        def fset(self, value):
            self._threadName = value
        return locals()
    threadName = property(**threadname())

    def threadkey():
        doc = "The threadKey property."

        def fget(self):
            return self._threadKey

        def fset(self, value):
            self._threadKey = value
        return locals()
    threadKey = property(**threadkey())

    def threadsettinghash_get(self):
        return self.threadsettinghash

    def threadsettinghash_set(self, value):
        self.threadsettinghash = value

    threadsettinghash = property(threadsettinghash_get, threadsettinghash_set)

    def getthreadsettinghashvalue(self, key):
        return self.threadsettinghash[key]

    def addthreadsettinghashvalue(self, key, value):
        self.threadsettinghash[key] = value

    def updatethreadsettinghashset(self, key, value):
        self.threadsettinghash.update({key, value})

    def removethreadsettinghashkey(self, key):
        self.threadsettinghash.pop(key)

    def readsetting(self):
        pass
