# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-10 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0375_auto_20200110_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remediationactionnotification',
            name='remediation_action',
        ),
        migrations.RemoveField(
            model_name='remediationactionnotification',
            name='sanction_outcome_comms_log_entry',
        ),
        migrations.DeleteModel(
            name='RemediationActionNotification',
        ),
    ]