# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-26 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('profiles', '0017_userprofile_migrated_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='admin_sites',
            field=models.ManyToManyField(related_name='admin_sites', to='wagtailcore.Site'),
        ),
    ]
