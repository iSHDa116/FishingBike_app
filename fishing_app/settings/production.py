import environ

from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env('DB_NAME'),
        "USER": env('DB_USER'),
        "PASSWORD": env('DB_PASSWORD'),  # 本番は必ず環境変数から
        "HOST": env('DB_HOST'),
        "PORT": env('DB_PORT', default='5432'),
    }
}