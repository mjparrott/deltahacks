# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltarelations', '0005_auto_20150215_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provided',
            name='Iid',
        ),
        migrations.RemoveField(
            model_name='provided',
            name='Uid1',
        ),
        migrations.DeleteModel(
            name='Provided',
        ),
        migrations.AddField(
            model_name='issues',
            name='delta_users',
            field=models.ManyToManyField(to='deltarelations.DeltaUser'),
            preserve_default=True,
        ),
    ]
