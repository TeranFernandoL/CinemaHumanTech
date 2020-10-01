from .base import *

DEBUG = True
SECRET_KEY = env('DJANGO_SECRET_KEY', default='z8j30%9q-jk9x!^j5q6#r+2bzc)#3kh#y-frt(5er+qpt-*en3')
ALLOWED_HOSTS = [
    "67.207.94.55"
]

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': "humantechdb",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': 'localhost',
        'PORT': '',
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
