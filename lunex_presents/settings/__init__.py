"""
Settings package for Lunex Presents.
Loads development settings by default. Set DJANGO_SETTINGS_MODULE
environment variable to 'lunex_presents.settings.production' for production.
"""
import os

environment = os.environ.get('DJANGO_ENV', 'development')

if environment == 'production':
    from .production import *
else:
    from .development import *
