# Generated by Django 5.0.2 on 2024-02-21 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission_handling', '0006_remove_submission_verdict'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='verdict',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
