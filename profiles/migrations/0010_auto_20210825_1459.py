# Generated by Django 3.2.6 on 2021-08-25 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210825_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
