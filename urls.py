import routers.mainHandler as main
import routers.postHandler as post
import routers.userHandler as user

urls = [
    (r'/', main.MainHandler),
    (r'/user/login', user.LoginHandler),
    (r'/post/(\d+)', post.PostHandler),
]
