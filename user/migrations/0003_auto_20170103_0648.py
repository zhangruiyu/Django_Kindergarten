# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170103_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
    ]
