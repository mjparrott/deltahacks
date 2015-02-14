# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import deltarelations.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeltaUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
                ('ethnicity', models.CharField(max_length=30)),
                ('religion', models.CharField(max_length=30)),
                ('relstat', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('issue', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('issue', models.ForeignKey(to='deltarelations.Issues')),
                ('provider', models.ForeignKey(to='deltarelations.DeltaUser', related_name='provider')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provided',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Iid', models.ForeignKey(to='deltarelations.Issues')),
                ('Uid1', models.ForeignKey(to='deltarelations.DeltaUser', related_name='uid1')),
                ('Uid2', models.ForeignKey(to='deltarelations.DeltaUser', related_name='uid2')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rating', models.IntegerField(validators=[deltarelations.models.validate_ratings])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='matches',
            name='ratings',
            field=models.ForeignKey(to='deltarelations.Ratings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matches',
            name='recipient',
            field=models.ForeignKey(to='deltarelations.DeltaUser', related_name='recipient'),
            preserve_default=True,
        ),
    ]
