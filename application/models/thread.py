#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

class Thread:
	"""docstring for Thread"""
	def __init__(self, arg):
		return self

	def threadName():
	    doc = "The threadName property."
	    def fget(self):
	        return self._threadName
	    def fset(self, value):
	        self._threadName = value
	    return locals()
	threadName = property(**threadName())

	def threadKey():
	    doc = "The threadKey property."
	    def fget(self):
	        return self._threadKey
	    def fset(self, value):
	        self._threadKey = value
	    return locals()
	threadKey = property(**threadKey())
