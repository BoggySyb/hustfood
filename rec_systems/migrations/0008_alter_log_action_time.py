# Generated by Django 3.2.8 on 2023-11-29 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_systems', '0007_auto_20231129_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action_time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 29, 13, 12, 51, 845260)),
        ),
    ]
