#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import modules.db

class MainHandler(tornado.web.RequestHandler):
    def get(self, pageSize=50, pageNum=1):
        posts = modules.db.db.query('select * from post')
        for post in posts:
            post.title_display = post.type and u'[求租]' + post.title or u'[出租]' + post.title

        self.render('index.html', posts=posts)
