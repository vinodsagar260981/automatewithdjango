from django import forms
from .models import Email

class EmailsForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ("email_list", "subject", "body", "attachment")