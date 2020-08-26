# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-15 07:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0382_auto_20200115_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalArtifactFormDataRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(blank=True, max_length=512, null=True)),
                ('schema_name', models.CharField(blank=True, max_length=256, null=True)),
                ('instance_name', models.CharField(blank=True, max_length=256, null=True)),
                ('component_type', models.CharField(choices=[('text', 'Text'), ('tab', 'Tab'), ('section', 'Section'), ('group', 'Group'), ('number', 'Number'), ('email', 'Email'), ('select', 'Select'), ('multi-select', 'Multi-Select'), ('text_area', 'Text Area'), ('table', 'Table'), ('expander_table', 'Expander Table'), ('label', 'Label'), ('radiobuttons', 'Radio'), ('checkbox', 'Checkbox'), ('declaration', 'Declaration'), ('file', 'File'), ('date', 'Date')], default='text', max_length=64)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('deficiency', models.TextField(blank=True, null=True)),
                ('physical_artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_data_records', to='wildlifecompliance.PhysicalArtifact')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='physicalartifactformdatarecord',
            unique_together=set([('physical_artifact', 'field_name')]),
        ),
    ]