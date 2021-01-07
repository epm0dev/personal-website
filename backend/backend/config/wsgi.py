import os
from django.core.wsgi import get_wsgi_application


# Set the settings module for the wsgi applcation and initialize the application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
