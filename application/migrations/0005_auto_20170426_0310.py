# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20170414_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='qoa',
            name='session',
            field=models.ForeignKey(to='application.Sessions'),
        ),
        migrations.AlterField(
            model_name='qoa',
            name='year',
            field=models.ForeignKey(to='application.Years'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
