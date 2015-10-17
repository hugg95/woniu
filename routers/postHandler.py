#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
from modules.db import db
import string
import constants
import baseHandler

class PostHandler(baseHandler.RequestHandler):
    @tornado.web.authenticated
    def get(self, id):
        query = 'select id, title, content, type, member_id, category_id, created, updated from post where id = %s'
        post = db.get(query, id)
        if post:
            author = db.get('select id, nick from member where id = %s', post.member_id)
            _category = '[' + constants.category[post.category_id]['name'] + ']'
            _type = ord(post.type)
            post.title_display = _type and u'[求租]' + _category + post.title or u'[出租]' + _category + post.title
            post.author = author

            self.render('post.html', post=post)

        raise tornado.web.HTTPError(404)

class ListHandler(baseHandler.RequestHandler):
    @tornado.web.authenticated
    def get(self, category=None, pageSize=50, pageNum=1):
        query = r'select id, title, member_id, type, category_id, created, updated from post order by if(updated is NULL, created, updated) desc'
        if category is not None:
            query = r'select id, title, member_id, type, category_id, created, updated from post where category_id = %d order by if(updated is NULL, created, updated) desc' % category
        posts = db.query(query)
        post_ids = []
        for post in posts:
            post_ids.append(str(post.id))
            _category = '[' + constants.category[post.category_id]['name'] + ']'
            _type = ord(post.type)
            post.title_display = _type and u'[求租]' + _category + post.title or u'[出租]' + _category + post.title
        if post_ids:
            authors = db.query('select id, nick from member where id in (' + ','.join(post_ids) + ')')
            for author in authors:
                for post in posts:
                    if author.id == post.member_id:
                        post.author = author

        self.render('index.html', posts=posts)

