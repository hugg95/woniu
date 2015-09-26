import tornado.ioloop
import tornado.web
import tornado.template
import os.path
import settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

if __name__ == '__main__':
    print settings.settings
    application = tornado.web.Application([
        (r'/', MainHandler),
    ], **settings.settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
