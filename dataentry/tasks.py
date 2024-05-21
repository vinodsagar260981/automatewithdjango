from awdmain.celery import app
from django.core.management import call_command
import time

from dataentry.utils import send_email_notification
# from django.core.mail import EmailMessage
from django.conf import settings

@app.task
def holdon_celery():
    time.sleep(10)
    #send an email
    mail_subject = 'Test Subject'
    message = 'This is a test email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Test Email is sent successfully'

@app.task
def import_data_task(full_path, model_name):
    try:
        call_command('importdata', full_path, model_name)
    except Exception as e:
        raise e
    #notify the user email
    mail_subject = 'Import Data completed'
    message = 'Your data import is successfully'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Task is completed successfully'