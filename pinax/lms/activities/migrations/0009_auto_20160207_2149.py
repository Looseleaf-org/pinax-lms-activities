# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 21:49
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_lms_activities', '0008_schema_fix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysessionstate',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='activitystate',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='userstate',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
    ]
