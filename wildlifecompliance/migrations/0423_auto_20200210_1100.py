# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-10 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0422_licencepurposedetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='licencepurposedetail',
            options={'ordering': ['index', 'purpose'], 'verbose_name': 'Licence purpose additional information', 'verbose_name_plural': 'Licence purpose additional information'},
        ),
    ]
