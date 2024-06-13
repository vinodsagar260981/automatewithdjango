from django.urls import path
from . import views

urlpatterns = [
    path('bulk-emails/', views.bulk_emails, name="bulk_emails"),
]