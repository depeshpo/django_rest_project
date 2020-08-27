from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '91t$m*gr^j-wetr-%ti02a!2g!ei)lhb*^ns*kb#)+oe0vz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    # configuration for django debug toolbar
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
        'rest_framework_swagger',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'  # django debug toolbar middleware
    ]
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(STATIC_MEDIA_DIR, 'db.sqlite3'),
    }
}
