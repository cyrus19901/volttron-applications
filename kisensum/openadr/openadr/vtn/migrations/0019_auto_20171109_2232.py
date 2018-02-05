# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 22:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0018_auto_20171109_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='drevent',
            name='event_id',
            field=models.IntegerField(default=0, verbose_name='Event ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drevent',
            name='last_status_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 22, 32, 1, 171480), null=True, verbose_name='Last Status Time'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_opt_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 22, 32, 1, 172517), null=True, verbose_name='Last opt-in'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_status_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 22, 32, 1, 172431), verbose_name='Last Status Time'),
        ),
    ]
