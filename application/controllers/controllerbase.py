#!/usr/bin/python2.7

import cgi
import cgitb
import os
import sys
import codecs
import Cookie



class ControllerBase(object):
	"""docstring for ControllerBase"""
	def __init__(self, title):
		super(ControllerBase, self).__init__()
		self.title = title
		return self
	
	def title_get(self):
	    return self._title
	def title_set(self, value):
	    self._title = value
	def title_del(self):
	    del self._title
	    return locals()

	title = property(title_get,title_set,title_del)

	def rawPostData():
	    doc = "The rawPostData property."
	    def fget(self):
	        return sys.stdin.read()
	    return locals()
	rawPostData = property(**rawPostData())

	def requestMethod():
	    doc = "The requestMethod property."
	    def fget(self):
	        return os.environ['REQUEST_METHOD']
	    return locals()
	requestMethod = property(**requestMethod())