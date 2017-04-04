# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 13:09
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170403_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish'), ('w', 'Withdrawn')], default='d', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도,위도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]
