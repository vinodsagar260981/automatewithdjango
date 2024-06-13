# Generated by Django 4.2.13 on 2024-06-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_subscriber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='attachment',
            field=models.FileField(blank=True, upload_to='email_attachments/'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email_address',
            field=models.EmailField(max_length=100),
        ),
    ]