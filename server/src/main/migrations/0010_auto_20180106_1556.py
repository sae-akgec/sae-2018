# Generated by Django 2.0 on 2018-01-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='theme_color',
            field=models.CharField(default='#84859d', max_length=10),
        ),
        migrations.AddField(
            model_name='workshop',
            name='theme_color',
            field=models.CharField(default='#84859d', max_length=10),
        ),
    ]
