import os
from django.core.asgi import get_asgi_application


# Set the settings module for the asgi applcation and initialize the application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_asgi_application()
