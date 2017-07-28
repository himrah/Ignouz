# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20170405_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='ans',
        ),
        migrations.AddField(
            model_name='answer',
            name='qes',
            field=models.ForeignKey(default='', to='application.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='qs',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
