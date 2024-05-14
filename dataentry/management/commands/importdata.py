from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import csv
#import the data using csv
#proposed custom command : python manage.py importdata path modelname

class Command(BaseCommand):
    help = "import the data into DB using CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Imported the data")
        parser.add_argument('model_name', type=str, help="Model name")


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        #search for model in all app
        model = None
        for app_config in apps.get_app_configs():
            #try
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        
        if not model:
            raise CommandError(f'Model "{model_name}" not found in apps')

        
        with open(file_path, 'r')as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Imported the data to DB using CSV file"))
