# Generated by Django 3.2 on 2021-05-06 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor_name', models.CharField(max_length=100, unique=True)),
                ('advisor_photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='AdvisorBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField(default=None)),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapp.advisor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
