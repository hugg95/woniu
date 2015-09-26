## application settings
##
## @author victor li
## @date 2015/09/26

import os.path

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')

settings = {
    'autoreload': True,
    'debug': True,
    'template_path': TEMPLATE_PATH
}
