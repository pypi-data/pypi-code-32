# Generated by Django 2.1.1 on 2018-09-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('um', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umprofile',
            name='night_mode',
        ),
    ]
