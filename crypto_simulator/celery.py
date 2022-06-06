import os

from celery import Celery

# Sets the path for django settings module for the Celery app to use it
# This allows for Django settings file to be used to configure Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_simulator.settings')

app = Celery('crypto_simulator')

# Variables than begins with 'CELERY' can be used to configure Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discovers task.py files from each Django app
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {repr(self.request)}')
