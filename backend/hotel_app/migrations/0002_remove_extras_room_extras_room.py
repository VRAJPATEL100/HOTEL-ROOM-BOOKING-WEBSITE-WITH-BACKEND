# Generated by Django 4.2.5 on 2023-09-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extras',
            name='room',
        ),
        migrations.AddField(
            model_name='extras',
            name='room',
            field=models.ManyToManyField(default='', related_name='extras', to='hotel_app.room'),
        ),
    ]
