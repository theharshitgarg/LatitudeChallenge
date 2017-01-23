# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='registration_type',
            field=models.CharField(choices=[('SF', 'Self'), ('GR', 'Group'), ('CP', 'Corporate'), ('OR', 'Others')], default='SF', max_length=2),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
