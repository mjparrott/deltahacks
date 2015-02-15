# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltarelations', '0002_auto_20150214_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='deltauser',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deltauser',
            name='last_name',
            field=models.CharField(default='oops', max_length=30),
            preserve_default=False,
        ),
    ]
