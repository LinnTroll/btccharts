"""Celery configuration."""
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btccharts.settings')

app = Celery('btcex')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-rates': {
        'task': 'core.tasks.get_markets',
        'schedule': crontab(minute=0),
    }
}
