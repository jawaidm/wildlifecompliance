# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-17 00:05
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0077_auto_20190416_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='application_type',
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]