# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-24 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0435_merge_20200221_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalcase',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('with_manager', 'With Manager'), ('with_prosecution_coordinator', 'With Prosecution Coordinator'), ('with_prosecution_coordinator_prosecution_brief', 'With Prosecution Coordinator (Prosecution Brief)'), ('with_prosecution_coordinator_court', 'With Prosecution Coordinator (Court)'), ('with_prosecution_council', 'With Prosecution Council'), ('with_prosecution_manager', 'With Prosecution Manager'), ('await_endorsement', 'Awaiting Endorsement'), ('discarded', 'Discarded'), ('brief_of_evidence', 'Brief of Evidence'), ('closed', 'Closed'), ('pending_closure', 'Pending Closure')], default='open', max_length=100),
        ),
    ]
