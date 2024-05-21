import csv
from django.core.management.base import BaseCommand, CommandParser
# from dataentry.models import Student
from django.apps import apps
import datetime
from dataentry.utils import generate_csv_file

#proposed command = python manage.py exportdata model_name

class Command(BaseCommand):
    help = "Export data from student model to a CSV file"


    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="Model name for importing csv file")
    
    def handle(self, *args, **kwargs):
        model_name = kwargs["model_name"].capitalize()

        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass

        if not model:
            self.stderr.write(f'Model {model_name} not found!')
            return

        #fetch the data from the database
        data = model.objects.all()
        # print(student)

        file_path = generate_csv_file(model_name)

        # #generate the timestamp
        # timestamp = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")

        # #file path make dynamic
        # file_path = f'exported_{model_name}_data_{timestamp}.csv'
        # # print(file_path)

        #open thes csv file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            #writes the csv header
            writer.writerow([field.name for field in model._meta.fields])

            #write the rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS("Data exported successfully"))