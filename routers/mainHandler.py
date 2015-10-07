import tornado.web
import modules.db

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        size = 50
        posts = modules.db.db.query('select * from post')
        self.render('index.html', posts=posts)
