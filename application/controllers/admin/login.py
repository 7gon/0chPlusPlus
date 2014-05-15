#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import libs.cherrypy.lib.sessions
import controllers.controllerbase
import hashlib


class Login(controllers.controllerbase.ControllerBase):
    def __init__(self):
        super(Login, self).__init__("admin.login")

    def loginaction(self, username, password):
        f = open("../../../application/config/user.cgi")
        for line in f:
            s = line.split("<>")
            if s[0] == username:
                rd = hashlib.sha512("<HASH-" + password + "gewrg>").hexdigest()
                if s[1] == rd:
                   # ses = libs.cherrypy.lib.sessions.Session()
                    return True
                else:
                    return False

        return False

    def viewaction(self):
        pass
