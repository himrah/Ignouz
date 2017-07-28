# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20170429_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoa',
            name='course',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
