# Generated by Django 4.1.13 on 2023-12-24 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_user_name_change',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
