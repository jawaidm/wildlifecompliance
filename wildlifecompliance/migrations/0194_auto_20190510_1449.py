# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-10 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0193_auto_20190509_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callemail',
            name='occurrence_time_from',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='callemail',
            name='occurrence_time_to',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
