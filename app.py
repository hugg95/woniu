import tornado.ioloop
import tornado.web
import tornado.template
import os.path
import settings
import routers.mainHandler
import routers.userHandler

if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', routers.mainHandler.MainHandler),
        (r'/user/login', routers.userHandler.LoginHandler),
    ], **settings.settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
