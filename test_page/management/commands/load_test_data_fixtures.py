import os

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

from wagtail.models import Page

class Command(BaseCommand):
    """ Command """
    help = 'Load Test Data Fixture'

    def add_arguments(self, parser):
        """ add_arguments """
        # no-output (optional) arguments
        parser.add_argument(
            '--no-output',
            action='store_true',
        )

    def handle(self, *args, **options):
        """ handle """
        self.no_output = options['no_output']

        User = get_user_model()
        username = os.environ.get('CMS_SUPERUSER_USERNAME', 'admin')
        if not User.objects.filter(username=username).exists():
            # Create superuser
            self.stdout.write('1 - Create superuser')
            password = os.environ.get('CMS_SUPERUSER_PASSWORD', 'admin')
            superuser = User.objects.create_superuser(username, None, password, id=8)
            self.stdout.write(self.style.SUCCESS('DONE'))

            # Remove Welcome Wagtail page
            self.stdout.write('2 - Remove Welcome Wagtail page')
            try:
                Page.objects.get(title='Welcome to your new Wagtail site!').delete()
            except Page.DoesNotExist:
                pass
            self.stdout.write(self.style.SUCCESS('DONE'))
