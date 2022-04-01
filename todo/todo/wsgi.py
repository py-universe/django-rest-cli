'''
WSGI config for todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
'''

import os
import pathlib

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

env_path = pathlib.Path('.').parent / '.env'
load_dotenv(dotenv_path=env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

application = get_wsgi_application()
