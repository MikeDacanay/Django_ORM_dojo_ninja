# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='book_authors.Books'),
        ),
    ]
