# Generated by Django 4.2.3 on 2023-07-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpms',
            name='info',
            field=models.JSONField(default=[{'Accomplishment': None, 'Activity': '', 'Indicator': '', 'Remarks': '', 'Target': None}]),
        ),
        migrations.AlterField(
            model_name='examinees',
            name='time',
            field=models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], max_length=2),
        ),
    ]
