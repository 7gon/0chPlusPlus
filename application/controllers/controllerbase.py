#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

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

    title = property(title_get, title_set)

    def rawpostdata():
        doc = "The rawPostData property."

        def fget(self):
            return sys.stdin.read()
        return locals()
    rawPostData = property(**rawpostdata())

    def requestmethod():
        doc = "The requestMethod property."

        def fget(self):
            return os.environ['REQUEST_METHOD']
        return locals()
    requestMethod = property(**requestmethod())


    def getcookie(self, key):
        co = Cookie.SimpleCookie()
        co.load(self.rawCookie)
        return co[key].value

    def rawcookie():
        doc = "The rawCookie property."

        def fget(self):
            return os.environ['HTTP_COOKIE']
        return locals()
    rawCookie = property(**rawcookie())