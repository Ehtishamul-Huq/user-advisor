# Generated by Django 3.2 on 2021-05-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('advisorapp', '0006_delete_advisorbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapp.advisor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
