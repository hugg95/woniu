#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import baseHandler
import hashlib
import modules.db
import datetime
import string
import constants

class LoginHandler(baseHandler.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        nick = self.get_body_argument('nick')
        password = self.get_body_argument('password')
        nick = nick.strip()
        if not nick or not password:
            self.write({'success': False, 'error_code': constants.error_code['miss_nick_or_password']})
            self.finish()
            return
        member = modules.db.db.get('select id, nick, password from member where nick = %s', nick)

        if member:
            md5 = hashlib.md5()
            md5.update(password)
            password_md5 = md5.hexdigest()
            if member.password == password_md5:
                self.write({'success': True, 'data': member})
                self.finish()
                return
        self.write({'success': False, 'error_code': constants.error_code['member_not_exist']})
        self.finish()

class SignupHandler(baseHandler.RequestHandler):
    def get(self):
        self.render('signup.html');

    def post(self):
        nick = self.get_body_argument('nick')
        password = self.get_body_argument('password')
        password_confirm = self.get_body_argument('password_confirm')
        nick = nick.strip()
        if nick and password and password_confirm:
            length = len(password)
            if length >=6 and length <= 18 and password == password_confirm:
                md5 = hashlib.md5()
                md5.update(password)
                password_md5 = md5.hexdigest()
                now = datetime.datetime.now()
                insert_sql = 'insert into member (nick, password, created) values (%s, %s, %s)'
                try:
                    member_id = modules.db.db.insert(insert_sql, nick, password_md5, now)
                    self.write({'success': True})
                    self.finish()
                    return
                except:
                    pass
                    # TODO add log

        self.write({'success': False})
        self.finish()

class ProfileHandler(baseHandler.RequestHandler):
    def get(self, id):
        user = modules.db.db.get('select id, nick, created, updated from member where id = %s', id)
        if user:
            self.render('profile.html', user=user)

        raise tornado.web.HTTPError(404)
