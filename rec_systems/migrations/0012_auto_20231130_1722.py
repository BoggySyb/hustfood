# Generated by Django 3.2.8 on 2023-11-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_systems', '0011_usercf_rec'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='sim_user_topk',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='sim_food_topk',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usercf_rec',
            name='rec_food_ids',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
