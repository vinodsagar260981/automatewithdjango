from django.core.management.base import BaseCommand, CommandParser
from django.apps import apps
import csv
import datetime

class Command(BaseCommand):
    help = "writing program to export csv"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="knowing the model name")

    def handle(self, *args, **kwargs):
        model_name = kwargs["model_name"].capitalize()

        timestamp = datetime.datetime.now().strftime("%y-%m-%d")
        
        # print(model_name)
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass

        if not model:
            self.stderr.write(f'model {model_name} not found!')
            return

        data = model.objects.all()

        filename = f'export_{model_name}_{timestamp}.csv'

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            #writes the csv header
            writer.writerow([field.name for field in model._meta.fields])

            #write the rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("Imported the CSV file"))