# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltarelations', '0003_auto_20150214_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provided',
            name='Uid2',
        ),
    ]
