from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import holdon_celery

def home(request):
    return render(request, 'home.html')

def celery_test(request):
    holdon_celery.delay()
    return HttpResponse('<h3>Function executed successfully</h3>')