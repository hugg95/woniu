#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author victor li nianchaoli@msn.cn
# @date 2015/10/15

import baseHandler
import json
from modules.db import db
import modules.utils

class ListHandler(baseHandler.RequestHandler):

    def get(self):
        post_id = self.get_argument('post_id')
        if not post_id:
            self.write(comments)
            self.finish()
            return

        query = 'select id, content, member_id, post_id, created, updated from comment where post_id = %s'
        _comments = db.query(query, post_id)
        if _comments:
            _comments = json.dumps(_comments, cls=modules.utils.JSONEncoder)
        comments = {'comments': _comments}

        self.write(comments)
        self.finish()

