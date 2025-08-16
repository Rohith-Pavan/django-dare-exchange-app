"""
WSGI config for dareproject project on PythonAnywhere.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""

import os
import sys

# Add your project directory to the sys.path
# Replace 'yourusername' with your actual PythonAnywhere username
path = '/home/yourusername/dareproject'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dareproject.pythonanywhere_settings')
os.environ.setdefault('DEBUG', 'False')
# Set your secret key in the PythonAnywhere web app environment variables instead
# os.environ.setdefault('SECRET_KEY', 'your-secret-key-here')

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
