#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import controllers.controllerbase


class AdminCgi(controllers.controllerbase.ControllerBase):
    def __init__(self):
        super(AdminCgi, self).__init__("admin.cgi")
