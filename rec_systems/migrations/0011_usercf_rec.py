# Generated by Django 3.2.8 on 2023-11-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_systems', '0010_alter_log_action_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCF_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('rec_food_ids', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
        ),
    ]
