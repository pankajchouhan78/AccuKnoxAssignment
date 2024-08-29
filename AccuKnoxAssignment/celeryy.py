from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AccuKnoxAssignment.settings')

# Create a Celery instance
celery_app = Celery('AccuKnoxAssignment')

# Using a string here means the worker does not have to serialize
# the configuration object to child processes.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()


# Set the timezone
celery_app.conf.timezone = 'Asia/Kolkata'

# Define the periodic task schedule
celery_app.conf.beat_schedule = {
    'send-ad-mail-every-day': {
        # 'task': 'send_email_celery.tasks.test', 
        'task': 'send_email_celery.tasks.send_scheduled_email', 
        # 'schedule': 5.0,
         'schedule': crontab(hour=11, minute=35),
    },    
}

@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
