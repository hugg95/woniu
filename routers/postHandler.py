#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import modules.db
import string
import constants

class PostHandler(tornado.web.RequestHandler):
    def get(self, id):
        id = string.atol(id)
        post = modules.db.db.get('select id, title, content, type, member_id, category_id, created, updated from post where id = %d' % id)
        author = modules.db.db.get('select id, nick, user_id from member where id = %d' % post.member_id)
        _category = '[' + constants.category[post.category_id]['name'] + ']'
        _type = ord(post.type)
        post.title_display = _type and u'[求租]' + _category + post.title or u'[出租]' + _category + post.title
        post.author = author

        self.render('post.html', post=post)
