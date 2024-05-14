from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "greets the user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies user name")

    def handle(self, *args, **kwargs):
        #greeting
        name = kwargs['name']
        greeting = f'Hello {name}, Good Morning'
        self.stdout.write(self.style.SUCCESS(greeting))