#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import controllers.controllerbase


class Login(controllers.controllerbase.ControllerBase):
    def __init__(self):
        super(Login, self).__init__("admin.login")

    def loginaction(self):
        pass

    def viewaction(self):
        pass