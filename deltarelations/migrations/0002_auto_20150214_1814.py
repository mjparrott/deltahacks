# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deltarelations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deltauser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='deltauser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='deltauser',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
