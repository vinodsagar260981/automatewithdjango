from django.shortcuts import render, redirect

from emails.tasks import send_email_task
from .forms import EmailsForm
from django.contrib import messages
from dataentry.utils import send_email_notification
from django.conf import settings
from .models import Subscriber

# Create your views here.
def bulk_emails(request):
    if request.method == "POST":
        email_form = EmailsForm(request.POST, request.FILES)
        if email_form.is_valid():
            email_form = email_form.save()
            #send email
            mail_subject = request.POST.get('subject')
            message = request.POST.get('body')
            to_email = settings.DEFAULT_TO_EMAIL

            #Access the selected email list
            email_list = request.POST.get('email_list')
            email_list = email_form.email_list
            # print(email_list)

            #extract email address from the subsriber model
            subscribers = Subscriber.objects.filter(email_list=email_list)

            to_email =[email.email_address for email in subscribers]

            
            if email_form.attachment:
                attachment = email_form.attachment.path
            else:
                attachment = None   

            send_email_task.delay(mail_subject, message, to_email, attachment)

            #display messages as success
            messages.success(request, 'Email sent succesfully !')
            return redirect('bulk_emails')

    else:
        email_form = EmailsForm()
        context = {
            'email_form' : email_form,
        }
    return render(request, 'emails/bulk_emails.html', context)