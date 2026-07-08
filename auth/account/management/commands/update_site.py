from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
import os

class Command(BaseCommand):
    help = 'Update site domain'

    def handle(self, *args, **kwargs):
        domain = os.environ.get("FRONTEND_URL", '127.0.0.1:3000')
        name = os.environ.get('SITE_NAME', 'Auth App')
        site = Site.objects.get(id=1)
        site.domain = name
        site.name = name
        site.save()
        self.stdout.write(f'Site updated tp {domain}')