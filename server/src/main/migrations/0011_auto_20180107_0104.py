# Generated by Django 2.0.1 on 2018-01-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180106_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organiser',
            name='contact_no',
        ),
        migrations.AddField(
            model_name='event',
            name='short_description',
            field=models.CharField(default='https://', max_length=400),
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='workshop',
            name='short_description',
            field=models.CharField(default='https://', max_length=400),
        ),
    ]
