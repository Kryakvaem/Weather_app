# Generated by Django 4.1 on 2022-08-17 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weater', '0002_alter_weather_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='data',
            field=models.DateField(default=datetime.datetime(2022, 8, 17, 15, 19, 56, 952770, tzinfo=datetime.timezone.utc)),
        ),
    ]
