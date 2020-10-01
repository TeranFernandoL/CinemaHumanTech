from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = [
    "67.207.94.55"
]

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
