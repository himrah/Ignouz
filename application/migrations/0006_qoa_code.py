# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20170426_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoa',
            name='code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
