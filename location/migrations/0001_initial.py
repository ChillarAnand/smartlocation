# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, default='')),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('language', models.CharField(blank=True, max_length=40)),
                ('currency', models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('polygon', djgeojson.fields.PolygonField()),
                ('provider', models.ForeignKey(to='location.Provider')),
            ],
        ),
    ]
