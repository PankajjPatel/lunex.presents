"""
Development settings for Lunex Presents.
"""
from .base import *  # noqa: F401, F403

DEBUG = True

SECRET_KEY = 'django-insecure-dev-key-lunex-presents-local-only'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', 'testserver']

# Use simple static file storage in development
STORAGES['staticfiles'] = {
    'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
}

# Database — SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Console email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
