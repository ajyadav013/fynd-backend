# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('popularity', models.DecimalField(decimal_places=1, max_digits=2)),
                ('director', models.CharField(max_length=100)),
                ('imdbScore', models.DecimalField(decimal_places=1, max_digits=1)),
                ('genre', models.ManyToManyField(to='movie.Genre')),
            ],
        ),
    ]
