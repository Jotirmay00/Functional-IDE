# Generated by Django 5.0.2 on 2024-02-18 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission_handling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
    ]
