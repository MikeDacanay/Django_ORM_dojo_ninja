# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20170815_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]