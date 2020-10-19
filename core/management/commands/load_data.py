from django.core.management.base import BaseCommand

from core.loader import load_data


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_data()
