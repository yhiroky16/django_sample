# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_companyassets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyassets',
            name='assets_no',
        ),
        migrations.AddField(
            model_name='companyassets',
            name='buyer',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
