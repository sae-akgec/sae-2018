# Generated by Django 2.0.1 on 2018-01-07 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_workshop_background_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='price',
        ),
    ]
