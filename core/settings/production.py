from core.settings.common import *

SECRET_KEY = get_env_variable("SECRET_KEY")
DEBUG = get_env_variable("DEBUG")

ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS")

# CORS https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_WHITELIST = get_env_variable("CORS_ORIGIN_WHITELIST")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable("DB_NAME"),
        'USER': get_env_variable("DB_USER"),
        'PASSWORD': get_env_variable("DB_PASSWORD"),
        'HOST': get_env_variable("DB_HOST"),
        'PORT': get_env_variable("DB_PORT"),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

# CELERY
BROKER_URL = get_env_variable("BROKER_URL")
CELERY_RESULT_BACKEND = get_env_variable("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
