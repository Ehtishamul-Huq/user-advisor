# Generated by Django 3.2 on 2021-05-08 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisorapp', '0003_alter_advisorbooking_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisorbooking',
            name='booking_time',
        ),
    ]
