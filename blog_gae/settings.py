from djangoappengine.settings_base import *
import os

DATABASES['default']['HIGH_REPLICATION'] = True

DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'


TIME_ZONE = 'Asia/Calcutta'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (

    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'blog',
    'django.contrib.admin',
    'registration',
    'django.contrib.humanize',
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)


TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

EMAIL_USE_TLS = True
EMAIL_HOST = 'monuvision.appspot.com'
EMAIL_HOST_USER = " "
EMAIL_HOST_PASSWORD = " "
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'smartdude.m69@gmail.com'
ACCOUNT_ACTIVATION_DAYS = 7


