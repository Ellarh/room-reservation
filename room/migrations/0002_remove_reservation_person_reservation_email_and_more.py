# Generated by Django 4.2.8 on 2023-12-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='person',
        ),
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='PersonBooking',
        ),
    ]
