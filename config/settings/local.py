from __future__ import absolute_import, unicode_literals

import os
import sys

from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#agido7mm*z&+o!dll)erh11&0_$-(y2+kuk3)t7z@6icw&1g^'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TESTING = sys.argv[1:2] == ['test']

def show_toolbar(request):
    return not TESTING  and bool(DEBUG)

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'incremental': True,
    'root': {
        'level': 'INFO',
    },
}

if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
        import debugpy
        debugpy.listen(("0.0.0.0", 3000))
        print('Attached!')

try:
    from .local import *
except ImportError:
    pass
