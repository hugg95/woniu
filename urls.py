import routers.baseHandler as base
import routers.mainHandler as main
import routers.postHandler as post
import routers.userHandler as user

urls = [
    (r'/', main.MainHandler),
    (r'/posts/last', post.ListHandler),
    (r'/post/(\d+)', post.PostHandler),
    (r'/user/login', user.LoginHandler),
    (r'/user/signup', user.SignupHandler),
    (r'/user/(\d+)', user.ProfileHandler),
    (r'.*', base.RequestHandler),
]
