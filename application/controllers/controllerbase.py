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
    def __init__(self, name):
        super(ControllerBase, self).__init__()
        self.name = name
        return self
    
    def name_get(self):
        return self._title

    def name_set(self, value):
        self._title = value

    name = property(name_get, name_set)

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

if __name__ == '__main__':
    import sys
    sys.stderr.write('Error: Don\'t call this file directly.')
    exit(-1)