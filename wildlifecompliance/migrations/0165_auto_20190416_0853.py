# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-16 00:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0164_merge_20190415_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callemail',
            options={'verbose_name': 'CM_Call/Email', 'verbose_name_plural': 'CM_Calls/Emails'},
        ),
        migrations.AlterModelOptions(
            name='classification',
            options={'verbose_name': 'CM_Classification', 'verbose_name_plural': 'CM_Classifications'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'CM_Location', 'verbose_name_plural': 'CM_Locations'},
        ),
        migrations.AlterModelOptions(
            name='referrer',
            options={'verbose_name': 'CM_Referrer', 'verbose_name_plural': 'CM_Referrers'},
        ),
        migrations.AlterModelOptions(
            name='reporttype',
            options={'verbose_name': 'CM_ReportType', 'verbose_name_plural': 'CM_ReportTypes'},
        ),
        migrations.AddField(
            model_name='reporttype',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reporttype',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='reporttype',
            name='replaced_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wildlifecompliance.ReportType'),
        ),
        migrations.AddField(
            model_name='reporttype',
            name='version',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='report_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='schema',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='reporttype',
            unique_together=set([('report_type', 'version')]),
        ),
    ]
