# Generated by Django 4.2.7 on 2023-11-16 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_systems', '0002_store_rename_img_food_imgurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='category',
            new_name='class1',
        ),
        migrations.AddField(
            model_name='food',
            name='class2',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
