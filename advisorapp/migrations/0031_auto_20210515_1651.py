# Generated by Django 3.2 on 2021-05-15 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('advisorapp', '0030_auto_20210515_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisorbooking',
            name='user',
        ),
        migrations.AddField(
            model_name='advisor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]