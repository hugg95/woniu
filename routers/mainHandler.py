#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import modules.db
import string

class MainHandler(tornado.web.RequestHandler):
    def get(self, pageSize=50, pageNum=1):
        posts = modules.db.db.query('select * from post')
        post_ids = []
        for post in posts:
            post_ids.append(str(post.id))
            type = ord(post.type)
            post.title_display = type and u'[求租]' + post.title or u'[出租]' + post.title
        if post_ids:
            authors = modules.db.db.query('select id, nick, user_id from member where id in (' + ','.join(post_ids) + ')')
            for author in authors:
                for post in posts:
                    if author.id == post.member_id:
                        post.author = author

        self.render('index.html', posts=posts)
