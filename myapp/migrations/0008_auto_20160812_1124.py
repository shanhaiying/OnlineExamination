# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_classroom_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 12, 11, 24, 5, 661319, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='mark',
            field=models.FloatField(default=70),
            preserve_default=False,
        ),
    ]
