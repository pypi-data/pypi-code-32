# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem_registration', '0006_auto_20181115_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdata',
            name='accounting_number',
            field=models.CharField(blank=True, default='', help_text='<details>для других страни или не используется или как-то иначе называется</details>', max_length=20, verbose_name='ЕГРПОУ'),
        ),
    ]
