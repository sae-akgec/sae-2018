# Generated by Django 2.0.1 on 2018-01-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20180110_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
    ]
