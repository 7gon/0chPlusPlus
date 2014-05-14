#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import controllerbase


class BbsCgi(controllerbase.ControllerBase):
    """docstring for BbsCgi"""
    def __init__(self):
        self.basedobject = controllerbase.ControllerBase.__init__(self, "bbs.cgi")

    basedobject = None

