# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20170811_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
    ]
