# Generated by Django 3.2.8 on 2023-12-03 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rec_systems', '0013_alter_log_action_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
