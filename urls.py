import routers.mainHandler as main
import routers.postHandler as post
import routers.userHandler as user

urls = [
    (r'/', main.MainHandler),
    (r'/posts/new', main.MainHandler),
    (r'/user/login', user.LoginHandler),
    (r'/user/signup', user.SignupHandler),
    (r'/user/(\d+)', user.ProfileHandler),
    (r'/post/(\d+)', post.PostHandler),
]
