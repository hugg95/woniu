import routers.mainHandler as main
import routers.userHandler as user

urls = [
    (r'/', main.MainHandler),
    (r'/user/login', user.LoginHandler),
]
