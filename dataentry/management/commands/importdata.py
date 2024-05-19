from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import csv

from django.db import DataError
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
        
        
        # get all the field names of the model 
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        # print(model_fields)
        
        with open(file_path, 'r')as file:
            reader = csv.DictReader(file)
            #compare csv names with model filed name
            csv_header = reader.fieldnames
            if csv_header != model_fields:
                raise DataError(f"CSV file is not matching with model {model_name}")

            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Imported the data to DB using CSV file"))
