# Generated by Django 3.2.8 on 2023-11-29 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rec_systems', '0008_alter_log_action_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action_time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 29, 13, 14, 51, 461644, tzinfo=utc)),
        ),
    ]
