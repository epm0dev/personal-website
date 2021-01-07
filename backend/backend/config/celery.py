import os
from celery import Celery


# Set the settings module for the celery application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize the celery application and autodiscover celery tasks
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
