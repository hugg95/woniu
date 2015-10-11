## application settings
##
## @author victor li
## @date 2015/09/26

import os.path

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')
STATIC_PATH = os.path.join(os.path.dirname(__file__), 'assets')

settings = {
    'autoreload': True,
    'debug': True,
    'compress_response': True,
    'template_path': TEMPLATE_PATH,
    'static_path': STATIC_PATH,
    'static_url_prefix': '/assets/'
}

db = {
    'host': '127.0.0.1',
    'database': 'db_woniu',
    'user': 'root',
    'password': 'test'
}
