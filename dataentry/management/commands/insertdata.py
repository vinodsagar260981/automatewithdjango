#insert data using an custom command
from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "insert data using an custom command"

    def handle(self, *args, **kwargs):

        datset = [
            {'roll_no':1002, 'name':"virat", 'age':32},
            {'roll_no':1003, 'name':"suresh", 'age':31},
            {'roll_no':1004, 'name':"dhoni", 'age':35},
            {'roll_no':1005, 'name':"srinath", 'age':45},
            {'roll_no':1006, 'name':"kumble", 'age':55},
        ]

        for data in datset:
            roll_no = data['roll_no']
            existing_data = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_data:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Roll no {roll_no} already exists!'))
        
        # #logic goes here
        # Student.objects.create(roll_no=1001, name="Sachin", age=31)
        self.stdout.write(self.style.SUCCESS("Data Inserted successfully!"))