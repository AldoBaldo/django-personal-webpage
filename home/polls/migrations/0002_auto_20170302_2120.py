# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
    ]
