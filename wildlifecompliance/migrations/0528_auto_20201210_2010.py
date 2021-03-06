# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-12-10 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0527_auto_20201210_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='penaltyamount',
            name='amount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='penaltyamount',
            name='amount_after_due',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='sanctionoutcome',
            name='penalty_amount_1st',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='sanctionoutcome',
            name='penalty_amount_2nd',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
    ]
