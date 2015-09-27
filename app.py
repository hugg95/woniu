import tornado.ioloop
import tornado.web
import tornado.template
import os.path
import settings
import routers.mainHandler

if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', routers.mainHandler.MainHandler),
    ], **settings.settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
