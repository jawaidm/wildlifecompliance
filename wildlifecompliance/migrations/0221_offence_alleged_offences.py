# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-11 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0220_auto_20190611_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='offence',
            name='alleged_offences',
            field=models.ManyToManyField(blank=True, to='wildlifecompliance.SectionRegulation'),
        ),
    ]
