#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web

class RequestHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            super(RequestHandler, self).write_error(status_code, **kwargs)
