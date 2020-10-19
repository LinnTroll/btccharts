"""Celery tasks"""

from celery.task import task

from core.loader import load_data


@task
def get_markets():
    """Celery task for loading data from API ib background."""
    load_data()
