# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-06-05 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0476_auto_20200531_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationselectedactivitypurpose',
            name='purpose_status',
            field=models.CharField(choices=[('default', 'Default'), ('current', 'Current'), ('expired', 'Expired'), ('cancelled', 'Cancelled'), ('surrendered', 'Surrendered'), ('suspended', 'Suspended'), ('replaced', 'Replaced')], default='default', max_length=40, verbose_name='Purpose Status'),
        ),
        migrations.AlterField(
            model_name='applicationselectedactivitypurpose',
            name='processing_status',
            field=models.CharField(choices=[('selected', 'Selected for Proposal'), ('propose', 'Proposed for Issue'), ('decline', 'Declined'), ('issue', 'Issued'), ('replace', 'Replaced'), ('reissue', 'Reissued')], default='selected', max_length=40, verbose_name='Processing Status'),
        ),
    ]
