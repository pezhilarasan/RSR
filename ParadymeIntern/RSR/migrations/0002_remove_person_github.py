# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='GitHub',
        ),
    ]
