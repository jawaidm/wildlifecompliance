# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-03-24 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0448_auto_20200320_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporttype',
            options={'verbose_name': 'CM_CallEmailReportType', 'verbose_name_plural': 'CM_CallEmailReportTypes'},
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='advice_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
