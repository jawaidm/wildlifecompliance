# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-28 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0492_remove_licencepurpose_apply_for_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wildlifelicencereceptionemail',
            old_name='address',
            new_name='email',
        ),
    ]