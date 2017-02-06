#!/usr/bin/env python
# -*- coding: utf8 -*-

#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#

"""
Module Description
"""

#
# Author: MingHe
#

from __future__ import print_function
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    Base handler
    """
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def set_default_headers(self):
        self.clear()
        # allow cross site
        self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json')
        result = {
            'errno': 0,
            'errmsg': 'OK'
        }
        self.write(result)
        self.finish()


class ExampleHandler(BaseHandler):
    """
    Base handler
    """
    def __init__(self, application, request, **kwargs):
        super(ExampleHandler, self).__init__(application, request, **kwargs)

    def get(self, *args, **kwargs):
        self.clear()
        id = self.get_argument('id', '123')
        result = {
            'errno': 0,
            'errmsg': 'OK'
        }
        self.write(result)
        self.finish()