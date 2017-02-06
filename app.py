#!/usr/bin/env python
# -*- coding: utf8 -*-

################################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
################################################################################

"""
Module Description
"""

#
# Author: MingHe
#

from __future__ import print_function
import os
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
from handlers.base_handler import *

STATIC_FILES = os.path.join(os.path.dirname(__file__), 'pages')

settings = {}

routes = [
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path":STATIC_FILES}),
    (r"/api/example", ExampleHandler),
    (r".*", BaseHandler)
]


class Application(tornado.web.Application):
    """Main Application

    Attribute
    """

    def __init__(self):
        """Init
        """
        tornado.web.Application.__init__(self, routes, **settings)


def main():
    """main

    Returns:
        TYPE: None
    """
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8661, "0.0.0.0")

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()