# Generated by Django 5.0.2 on 2024-02-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission_handling', '0004_remove_submission_test_cases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.CharField(blank=True, default='Passed', max_length=50),
        ),
    ]
