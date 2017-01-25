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

    def get(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json')
        result = {
            'errno': 0,
            'errmsg': 'OK'
        }
        self.write(result)
        self.finish()