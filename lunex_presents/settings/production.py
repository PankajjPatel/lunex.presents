
"""
Production settings for Lunex Presents.
All sensitive values come from environment variables.
"""

from .base import *  # noqa: F401, F403

# --------------------------------------------------
# Environment & Security
# --------------------------------------------------

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = [
    'lunexpresents.vercel.app',
    '.vercel.app',
]

CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS',
    default=[
        'https://lunexpresents.vercel.app',
    ],
)

# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASES = {
    'default': env.db(
        'DATABASE_URL',
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
    ),
}

# --------------------------------------------------
# HTTPS & Browser Security
# --------------------------------------------------

SECURE_SSL_REDIRECT = env.bool(
    'SECURE_SSL_REDIRECT',
    default=True,
)

SECURE_PROXY_SSL_HEADER = (
    'HTTP_X_FORWARDED_PROTO',
    'https',
)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# --------------------------------------------------
# Static Files
# --------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --------------------------------------------------
# Email
# --------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
