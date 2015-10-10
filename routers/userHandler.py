#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('signup.html');
