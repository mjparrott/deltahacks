# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltarelations', '0004_remove_provided_uid2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provided',
            name='Iid',
            field=models.ForeignKey(to='deltarelations.Issues', related_name='iid'),
            preserve_default=True,
        ),
    ]
