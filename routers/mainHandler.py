#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author victor li nianchaoli@msn.cn
# @date 2015/10/07

import baseHandler

class MainHandler(baseHandler.RequestHandler):

    def get(self):
        self.redirect('/posts/last')
