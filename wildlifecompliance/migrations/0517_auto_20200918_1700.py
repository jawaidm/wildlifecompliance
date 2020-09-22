# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-18 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0516_applicationstandardcondition_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purposespecies',
            name='species',
        ),
        migrations.AddField(
            model_name='purposespecies',
            name='is_additional_info',
            field=models.BooleanField(default=False),
        ),
    ]