#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import modules.db

class RequestHandler(tornado.web.RequestHandler):

    def get(self):
        raise tornado.web.HTTPError(404)

    def get_current_user(self):
        return self.get_cookie('current_user');

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            super(RequestHandler, self).write_error(status_code, **kwargs)
