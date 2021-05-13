# Generated by Django 3.2 on 2021-05-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('advisorapp', '0009_remove_advisorbooking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisorbooking',
            name='advisor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='advisorapp.advisor'),
        ),
        migrations.AddField(
            model_name='advisorbooking',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
