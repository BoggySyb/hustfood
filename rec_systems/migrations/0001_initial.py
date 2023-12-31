# Generated by Django 4.2.7 on 2023-11-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('category', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('position', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('price', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('img', models.URLField(blank=True, max_length=256)),
            ],
        ),
    ]
