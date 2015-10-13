import routers.baseHandler as base
import routers.mainHandler as main
import routers.postHandler as post
import routers.userHandler as user

urls = [
    (r'/', main.MainHandler),
    (r'/posts/last', post.ListHandler),
    (r'/posts/(\d+)', post.PostHandler),
    (r'/users/login', user.LoginHandler),
    (r'/users/signup', user.SignupHandler),
    (r'/users/(\d+)', user.ProfileHandler),
    (r'.*', base.RequestHandler),
]
