from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import logging
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hyre.settings')

app = Celery('Hyre', broker='amqp://guest@localhost//')
app.conf.broker_connection_retry_on_startup = True

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'Check interview remaining time': {
        'task': 'Scheduler.tasks.check_interview',
        'schedule': timedelta(seconds=50),
    }
    
}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# @app.task
# def my_task():
#     logging.info('Task started')
#     # Do some work
#     logging.info('Task completed')