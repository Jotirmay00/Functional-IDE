# Generated by Django 5.0.2 on 2024-02-20 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission_handling', '0005_alter_submission_verdict'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='verdict',
        ),
    ]
