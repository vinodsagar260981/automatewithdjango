# Generated by Django 4.2.13 on 2024-06-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=50)),
                ('email_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.list')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('attachment', models.FileField(upload_to='email_attachments/')),
                ('email_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.list')),
            ],
        ),
    ]
