# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-25 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0015_static_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='matched_count_updated_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='matched_users_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
