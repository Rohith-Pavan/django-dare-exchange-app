"""
PythonAnywhere-specific settings for dareproject.
This file contains production settings for PythonAnywhere deployment.
"""

from dareproject.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update ALLOWED_HOSTS for your PythonAnywhere domain
# Replace 'yourusername' with your actual PythonAnywhere username
ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',
    'www.yourusername.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# Static files configuration for PythonAnywhere
# Replace 'yourusername' with your actual PythonAnywhere username
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/dareproject/staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Use WhiteNoise for static files serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/dareproject/media'

# Database configuration for PythonAnywhere
# Using SQLite for simplicity - you can upgrade to MySQL on paid plans
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For MySQL (available on paid plans), uncomment and configure:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'yourusername$dareproject',
#         'USER': 'yourusername',
#         'PASSWORD': 'your-mysql-password',
#         'HOST': 'yourusername.mysql.pythonanywhere-services.com',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Session security
SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
CSRF_COOKIE_SECURE = False     # Set to True if using HTTPS

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/home/yourusername/dareproject/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
